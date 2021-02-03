from cbot.client     import CbClient
from cbot.model      import Order

class Cbot:
    trend = 'd' # assume on start so we don't buy right away
    min_price = 35
    margin = 0.011
    purchase_percentage = 0.05

    def __init__(self):
        self.client = CbClient()
        self._update_balances()
        self.price = self.client.current_coin_price()
        self.purchase_size = self._calculate_purchase_size()
        self._reset_extreme_counts()
        self._reset_runs_since_last()
        self._reset_runs_in_price_box()
        self._set_ceiling()
        self._set_floor()

    def test_run(self):
        self._sell_all_coin()

    def _sell_all_coin(self):
        amt = self.client.coin_balance()
        self.client.place_market_sale(amt)

    def __call__(self, price, runs):
        self.runs = runs
        if price is None:
            return 0
        else:
            self.price = float(price)
            try: 
                return self._run()
            except:
                pass

    def _run(self):
        self._make_money()
        self._default_report()
        self._handle_run_count()

    def _default_report(self):
        if self.runs % 10 == 0:
            print('--------------default 100th---------------')
            self._report()

    def _handle_run_count(self):
        self.runs += 1
        if self.runs % 100 == 0:
            self._adjust_purchase_size()
            self.runs = 2

    def _report(self):
        print('market: '           + 'BTC-USD')
        print('runs: '             + str(self.runs))
        print('**')
        print('Coin price: '       + str(self.price))
        print('ceiling: '          + str(self.ceiling))
        print('floor: '            + str(self.floor))
        print('ceiling diff: '     + str(self._ceiling_diff()))
        print('floor diff: '       + str(self._floor_diff()))
        print('**')
        print('Trend: '            + self.trend)
        print('stabilized: '       + self._stablabized())
        print('runs in price box:' + str(self.runs_in_price_box))
        print('**')
        print('Coin balance: '     + str(self.coin_balance))
        print('USD balance: '      + str(self.usd_balance))
        print('cash out value: '   + str(self._cash_out_value()))
        print('purchase size: '    + str(self.purchase_size))

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
        return self.runs_in_price_box >= 1000

    def _reset_runs_since_last(self):
        self.runs_since_last_transaction = 0

    def _reset_runs_in_price_box(self):
        self.runs_in_price_box = 0

    def _ceiling_diff(self):
        return self.price - self.ceiling

    def _floor_diff(self):
        return self.price - self.floor

    def _cash_out_value(self):
        return self.coin_balance * self.price + self.usd_balance

    def _adjust_purchase_size(self):
        self._set_purchase_size()
        print('purchase size set to: ' + str(self.purchase_size))

    def _update_limits(self):
        if self.price > self.ceiling or self.price < self.floor:
            self._set_ceiling()
            self._set_floor()
            self._reset_runs_in_price_box()

    def _set_purchase_size(self):
        self.purchase_size = round(self._calculate_purchase_size(), 2)

    def _make_money(self):
        self._update_balances()
        self._monitor_trend()
        self._run_transactions()
        self._update_pending_orders()
        self._update_limits()

    def _update_balances(self):
        self.coin_balance = self.client.coin_balance()
        self.usd_balance = self.client.usd_balance()

    def _run_buys(self):
        self._place_order(self.purchase_size)
        self.last_transaction_rate = self.price
        self._reset_runs_since_last()

    def _place_order(self, amount):
        result = self.client.place_market_buy(amount)
        print('####### buy API result #########')
        print(result)
        return Order.create(result)

    def _run_transactions(self):
        if self._time_to_buy():
            self._buy_report()
            self._run_buys()
        elif self._time_to_sell():
            self._sell_report()
            self._run_sales()
        else:
            self.runs_since_last_transaction += 1

    def _buy_report(self):
        print('+++++++++++++++++ TIME TO BUY ++++++++++++++++++')
        print('    new valley: '          + str(self._new_valley()))
        print('        trend: '           + self.trend)
        print('        runs_in_valley: '  + str(self.runs_in_valley))
        print('    moving_steadily_up: '  + str(self._moving_steadily_up()))
        print('        above_ceiling: : ' + str(self._above_ceiling()))
        print('    new_up_trend: '        + str(self._new_up_trend()))
        print('        new_trend: '       + str(self.new_trend))
        self._report()

    def _sell_report(self):
        print('+++++++++++++++++ TIME TO SELL ++++++++++++++++++')
        print('    _new_peak: '        + str(self._new_peak()))
        print('        trend: '        + self.trend)
        print('        runs_at_peak: ' + str(self.runs_at_peak))
        print('    _new_down_trend: '  + str(self._new_down_trend()))
        print('        new_trend: '    + str(self.new_trend))
        self._report()

    def _monitor_trend(self):
        self._check_for_turns()
        self._check_for_extremes()

    def _check_for_turns(self):
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
            self.runs_in_price_box += 1

    def _check_for_extremes(self):
        if self._holding_in_valley():
            self.runs_in_valley += 1
        elif self._holding_at_peak():
            self.runs_at_peak += 1
        else:
            self._reset_extreme_counts()

    def _reset_extreme_counts(self):
        self.runs_at_peak = 0
        self.runs_in_valley = 0

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
        return self._valley_or_uptick()  and not self._peaked()

    def _valley_or_uptick(self):
        return self._new_valley() or self._moving_steadily_up() or self._new_up_trend()

    def _peaked(self):
        return self._holding_at_peak() or self._new_peak()

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
            cb_record = self.client.get_order(order.external_id)
            if self._needs_update(cb_record.get('status'), order.status):
                order.execute(cb_record)

    def _run_sales(self):
        self._execute_sales()
        self.last_transaction_rate = self.price
        self._reset_runs_since_last()

    def _execute_sales(self):
        total_to_sell = 0.0
        for order in Order.profitable(self.price):
            total_to_sell += (order.filled_size or 0)

        if total_to_sell > 0:
            rounded_total = round(total_to_sell, 8)
            result = self.client.place_market_sale(rounded_total)
            new_order = Order.create(result)
