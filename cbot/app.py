from cbot.client     import Client
from cbot.model      import Order
from cbot.transactor import Transactor
from cbot.db         import session

class Cbot:
    usd_buy_amount = 100

    def __init__(self):
        self.uninitialized = True
        self.client        = Client()
        self.transactor    = Transactor(self.client)
        self.runs          = 0

    def __call__(self, price):
        if price is None:
            return
        else
            self.price = price
            self._run()

    def _run(self):
        if self.runs == 0:
            self._first_pass_setup()
            self.runs == 1
        else if self.runs == 1
            self._second_pass_setup()
            self.runs == 2
        else
            self._make_money()

    def _first_pass_setup(self):
        self.price                  = self.price
        self.last_trasnsaction_rate = self.price
        self.uninitialized          = False
        self._set_ceiling()
        self._set_floor()

    def _second_pass_setup(self):
        if self.price > self.last_transaction_rate
            self.trend = 'up'
        else self.price <= self.last_transaction_rate
            self.trend = 'down'

    def _make_money(self):
        self._run_transactions()
        self._monitor_trend()
        self._update_pending_orders()

    def _run_transactions(self):
        if self._time_to_buy():
            self.transactor.market_buy(self.usd_buy_amount)
            self._last_transaction_rate = self.price
        else if self._time_to_sell():
            self._execute_sales()
            self._last_transaction_rate = self.price
        else
            pass

    def _monitor_trend(self)
        if self._new_down_trend():
            self.trend = 'down'
        else self._new_up_trend():
            self.trend = 'up'

    def _new_down_trend(self):
        self.trend == 'up' && self._below_floor()

    def _new_up_trend(self):
        self.trend == 'down' and self._above_ceiling()

    def _time_to_sell(self):
        # reversal of upward tren
        self.trend == 'up' and self._below_floor()

    def _time_to_buy(self):
        self._moving_steadily_up() or self._moving_steadily_down()

    def _moving_steadily_up(self):
        return self.trend == 'up' and self._above_ceiling()

    def _moving_steadily_down(self):
         return self.trend == 'below' and self._below_floor()

    def _below_floor(self):
        self.price <= self.floor

    def _above_ceilng(self):
        return self.price >= self.ceiling

    def _set_ceiling(self):
        return self.ceiling = self.price * 0.02 + self.price

    def _set_floor(self):
        self.floor = self.price - self.price * 0.04

    def _execute_sales(self):
        for order in self._profitable_orders():
            self.transactor.sell(order)

    def _update_pending_orders(self):
        for order in Order.pending():
            cb_record = self.client.get_order(order.external_id)

            if self._needs_update(cb_record.get('status'), order.status):
                order.execute_purchase(cb_record)

    def _needs_update(self, ext_status, int_status):
        return ext_status != 'pending' and ext_status != int_status

    def _profitable_orders(self):
        return Order.profitable(self.current_price)
