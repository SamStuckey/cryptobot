from cbot.client     import Client
from cbot.model      import Order

class Cbot:
    trend = 'd' # assume on start so we don't buy right away
    min_price = 35
    margin = 0.015
    purchase_percentage = 0.05

    def __init__(self):
        self.client = Client()
        self.price = self.client.current_btc_price()
        self._update_balances()
        self.purchase_size = self._calculate_purchase_size()
        self._reset_extreme_counts()
        self._reset_runs_since_last()
        self._set_ceiling()
        self._set_floor()

    def test_run(self):
        pass
        #  self._sell_all_btc()
        #  self.price = float(self.client.current_btc_price())
        #  print(self._place_order(self.min_price))
        #  self._update_pending_orders()
        #  self._execute_sales()
        #  self._update_pending_orders()

    def __call__(self, price, runs):
        self.runs = runs
        if price is None:
            return 0
        else:
            self.price = float(price)
            return self._run()

    def _run(self):
        self._make_money()
        self._report()
        self._handle_run_count()

    def _handle_run_count(self):
        self.runs += 1
        if self.runs == 10:
            self.adjust_purchase_size()
            self.runs = 2

    def _report(self):
        if self.runs % 10 == 0:
            print('--------------------------------------')
            print('runs: '           + str(self.runs))
            print('BTC balance: '    + str(self.btc_balance))
            print('USD balance: '    + str(self.usd_balance))
            print('BTC price: '      + str(self.price))
            print('ceiling: '        + str(self.ceiling))
            print('floor: '          + str(self.floor))
            print('ceiling diff: '   + str(self._ceiling_diff()))
            print('floor diff: '     + str(self._floor_diff()))
            print('Trend: '          + self.trend)
            print('cash out value: ' + str(self._cash_out_value()))
            print('stabalized: '     + self._stablabized())
            print('purchase size: '  + str(self.purchase_size))
            print('--------------------------------------')

    def _stablabized(self):
        if self._holding_at_peak():
            return 'peak'
        elif self._holding_in_valley():
            return 'valley'
        else:
            return 'False'

    def _holding_at_peak(self):
        return self._holding() and self.trend == 'u'

    def _holding_in_valley(self):
        return self._holding() and self.trend == 'd'

    def _holding(self):
        return self.runs_since_last_transaction >= 100

    def _reset_runs_since_last(self):
        self.runs_since_last_transaction = 0

    def _ceiling_diff(self):
        return self.price - self.ceiling

    def _floor_diff(self):
        return self.price - self.floor

    def _cash_out_value(self):
        return self.btc_balance * self.price + self.usd_balance

    def adjust_purchase_size(self):
        self._set_purchase_size()

    def _update_limits(self):
        if self.price > self.ceiling or self.price < self.floor:
            self._set_ceiling()
            self._set_floor()

    def _set_purchase_size(self):
        self.purchase_size = round(self._calculate_purchase_size(), 2)

    def _make_money(self):
        self._update_balances()
        self._monitor_trend()
        self._run_transactions()
        self._update_pending_orders()
        self._update_limits()

    def _update_balances(self):
        self.btc_balance = self.client.btc_balance()
        self.usd_balance = self.client.usd_balance()

    def _run_buys(self):
        self._place_order(self.purchase_size)
        self.last_transaction_rate = self.price
        self._reset_runs_since_last()

    def _place_order(self, amount):
        result = self.client.place_market_buy(amount)
        return Order.create(result)

    def _run_sales(self):
        self._execute_sales()
        self.last_transaction_rate = self.price
        self._reset_runs_since_last()

    def _run_transactions(self):
        if self._time_to_buy():
            print('time to buy')
            self._run_buys()
        elif self._time_to_sell():
            print('time to sell')
            self._run_sales()
        else:
            self.runs_since_last_transaction += 1

    def _monitor_trend(self):
        if self._down_turn():
            print('down turn')
            self.trend = 'd'
            self.new_trend = True
            self._reset_extreme_counts()
        elif self._up_turn():
            print('up turn')
            self.trend = 'u'
            self.new_trend = True
            self._reset_extreme_counts()
        else:
            self.new_trend = False

        if self._holding_in_valley():
            self.runs_in_valley += 1
            if self.runs_in_valley % 100 == 0:
                print('holding valley: ' + str(self.runs_in_valley))
        elif self._holding_at_peak():
            self.runs_at_peak += 1
            if self.runs_at_peak % 100 == 0:
                print('holding peak: ' + str(self.runs_in_valley))
        else:
            self._reset_extreme_counts()

    def _reset_extreme_counts(self):
        self.runs_at_peak = 0
        self.runs_in_valley = 0

    #  [wipn] START HERE - getting false positives for time to sell... figure out why
    def _time_to_sell(self):
        return self._new_peak() or self._new_down_trend()

    def _new_down_trend(self):
        return self.trend == 'd' and self.new_trend

    def _new_up_trend(self):
        return self.trend == 'u' and self.new_trend

    def _up_turn(self):
        return self.trend == 'd' and self._above_ceiling()

    def _down_turn(self):
        return self.trend == 'u' and self._below_floor()

    def _time_to_buy(self):
        return self._purchase_rules_apply() and self._funds_available()

    def _purchase_rules_apply(self):
        return self._new_valley() or self._moving_steadily_up() or self._new_up_trend()

    def _new_peak(self):
        return self.trend == 'u' and (self.runs_at_peak == 101)

    def _new_valley(self):
        return self.trend == 'd' and (self.runs_in_valley == 101)

    def _funds_available(self):
        return self.usd_balance >= self.purchase_size

    def _moving_steadily_up(self):
        return self.trend == 'u' and self._above_ceiling()

    def _moving_steadily_down(self):
         return self.trend == 'd' and self._below_floor()

    def _below_floor(self):
        return self.price <= self.floor

    def _above_ceiling(self):
        return self.price >= self.ceiling

    def _needs_update(self, ext_status, int_status):
        return ext_status != 'pending' and ext_status != int_status

    def _calculate_purchase_size(self):
        percentage_based = self.usd_balance * self.purchase_percentage
        if percentage_based < self.min_price:
            return self.min_price
        else:
            return percentage_based

    def _set_ceiling(self):
        self.ceiling = self.price * self.margin + self.price

    def _set_floor(self):
        self.floor = self.price - self.price * self.margin

    def _update_pending_orders(self):
        for order in Order.pending():
            print(order.status)
            cb_record = self.client.get_order(order.external_id)
            if self._needs_update(cb_record.get('status'), order.status):
                order.execute(cb_record)

    def _execute_sales(self):
        total_to_sell = 0.0
        for order in Order.profitable(self.price):
            total_to_sell += (order.filled_size or 0)
        if total_to_sell > 0:
            rounded_total = round(total_to_sell, 8)
            result = self.client.place_market_sale(rounded_total)
            Order.create(result)

    def _sell_all_btc(self):
        amt = self.client.btc_balance()
        self.client.place_market_sale(amt)
