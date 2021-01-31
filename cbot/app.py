from cbot.client     import Client
from cbot.model      import Order
from cbot.db         import session

class Cbot:
    trend = 'down' # assume on start so we don't buy right away

    def __init__(self):
        self.client = Client()
        self.price = self.client.current_btc_price()
        self.purchase_size = self._calculate_purchase_size()
        self._reset_extreme_counts()
        self._reset_runs_since_last()
        self._update_limits()

    def test_run(self):
        self.price = float(self.client.current_btc_price())
        print(self.price)
        #  sale_result = self.client.place_market_sale(5)
        #  buy_result = self.client.place_market_buy(5)
        #  order_query_result = self.client.get_order(foobar)
        #  print(sale_result)
        #  print(buy_result)
        #  print(order_query_result)

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
        if self.runs == 1000:
            self.adjust_purchase_size()
            self.runs = 2

    def _report(self):
        if self.runs % 10 == 0:
            self.btc_balance = self.client.btc_balance()
            self.usd_balance = self.client.usd_balance()
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
        return self._holding() and self.trend == 'up'

    def _holding_in_valley(self):
        return self._holding() and self.trend == 'down'

    def _holding(self):
        return self.runs_since_last_transaction >= 1000

    def _reset_runs_since_last(self):
        self.runs_since_last_transaction = 0

    def _ceiling_diff(self):
        return self.price - self.ceiling

    def _floor_diff(self):
        return self.price - self.floor

    def _cash_out_value(self):
        return self.btc_balance * self.price + self.usd_balance

    def adjust_purchase_size(self):
        if self._double_profit():
            self._set_purchase_size()

    def _double_profit(self):
        return self.client.usd_balance >= self.purchase_size * 200

    def _update_limits(self):
        self._set_ceiling()
        self._set_floor()

    def _set_purchase_size(self):
        self.purchase_size = round(self._calculate_purchase_size(), 2)

    def _make_money(self):
        self._monitor_trend()
        self._run_transactions()
        self._update_pending_orders()

    def _run_buys(self):
        #  self.client.place_market_buy(self.purchase_size)
        self._last_transaction_rate = self.price
        self._update_limits()
        self._reset_runs_since_last()

    def _run_sales(self):
        #  self._execute_sales()
        self._last_transaction_rate = self.price
        self._update_limits()
        self._reset_runs_since_last()


    def _run_transactions(self):
        if self._time_to_buy():
            self._run_buys()
        elif self._time_to_sell():
            self._run_sales()
        else:
            self.runs_since_last_transaction += 1

    def _monitor_trend(self):
        if self._new_down_trend():
            self.trend = 'down'
            self._reset_extreme_counts()
        elif self._new_up_trend():
            self.trend = 'up'
            self._reset_extreme_counts()

        if self._holding_in_valley():
            self.runs_in_valley += 1
        elif self._holding_at_peak():
            self.runs_at_peak += 1
        else:
            self._reset_extreme_counts()

    def _reset_extreme_counts(self):
        self.runs_at_peak = 0
        self.runs_in_valley = 0

    def _new_up_trend(self):
        return self.trend == 'down' and self._above_ceiling()

    def _time_to_sell(self):
        self._new_peak() or self._new_down_trend()

    def _new_down_trend(self):
        return self.trend == 'up' and self._below_floor()

    def _time_to_buy(self):
        return self._purchase_rules_apply() and self._funds_available()

    def _purchase_rules_apply(self):
        return self._new_valley() or self._moving_steadily_up()

    def _new_peak(self):
        # arbitrary time at peak, but check twice incase of race conditions
        return self.trend == 'up' and (self.runs_at_peak == 1001 or self.runs_at_peak == 1111)

    def _new_valley(self):
        # buy twice on long valleys
        return self.trend == 'down' and (self.runs_in_valley == 1001 or self.runs_in_valley == 10001)

    def _funds_available(self):
        return self.usd_balance() >= self.purchase_size

    def _moving_steadily_up(self):
        return self.trend == 'up' and self._above_ceiling()

    def _moving_steadily_down(self):
         return self.trend == 'down' and self._below_floor()

    def _below_floor(self):
        return self.price <= self.floor

    def _above_ceiling(self):
        return self.price >= self.ceiling

    def _needs_update(self, ext_status, int_status):
        return ext_status != 'pending' and ext_status != int_status

    def _profitable_orders(self):
        return Order.profitable(self.current_price)

    def _calculate_purchase_size(self):
        return self.client.usd_balance() * float(0.05)

    def _set_ceiling(self):
        self.ceiling = self.price * 0.02 + self.price

    def _set_floor(self):
        self.floor = self.price - self.price * 0.02

    def _execute_sales(self):
        total_to_sell = 0
        for order in self._profitable_orders():
            total_to_sell = total_to_sell + float(order['btc_quantity'])
            #  [wipn] implement this
            order.mark_sale_pending()

        if total_to_sell > 0:
            self.client.place_market_sale(total_to_sell)

    #  [wipn] will this work for pending sales as well?
    def _update_pending_orders(self):
        for order in Order.pending():
            cb_record = self.client.get_order(order.external_id)

            if self._needs_update(cb_record.get('status'), order.status):
                order.execute_purchase(cb_record)
