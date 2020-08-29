from cbot.client     import Client
from cbot.model      import Order
from cbot.transactor import Transactor
import time
from cbot.db import session

class Cbot:
    btc_purchase_increment = 10
    usd_buy_amount         = 5
    btc_required_increase  = 50

    def __init__(self):
        self.client     = Client()
        self.transactor = Transactor(self.client)

    #  [wipn] testing call
    #  def __call__(self, price):
    #      cb_rec = {'id': 'd3508523-78a9-4a1e-a9e2-eb9054527608', 'product_id': 'BTC-USD',
    #              'side': 'buy', 'stp': 'dc', 'funds': '9.95024875', 'specified_funds': '10',
    #              'type': 'market', 'post_only': False, 'created_at': '2020-07-19T15:36:39.654557Z', 'fill_fees': '0',
    #              'filled_size': '0', 'executed_value': '0', 'status': 'pending', 'settled': False}

    #  [wipn] - keep
    def __call__(self, price):
        if price is not None:
            self.price = price

            #  [wipn] not tested yet
            #  self._execute_sales()

            #  [wipn] this works
            #  self._execute_purchase()

            time.sleep(1)
            self._update_pending_orders()

    def _execute_sales(self):
        self._sell_all_profitable_orders()

    #  [wipn] START HERE - saving works on session, but never persists to PG
    def _update_pending_orders(self):
        for order in Order.pending():
            cb_record = self.client.get_order(order.external_id)
            if cb_record.get('status') != 'pending':
                order.update_from_cb(cb_record)

    def _execute_purchase(self):
        if self._time_to_buy():
            self.transactor.market_buy(self.usd_buy_amount)

    def _set_limit_sale(self, order):
        sell_price = new_order.buy_btc_val + self.btc_required_increase
        self.transactor.place_limit_sale(new_order, sell_price=sell_price)

    #  [wipn] this probably doesn't need to happen, if i just set market sell orders
    #  when i buy
    def _sell_all_profitable_orders(self):
        for order in self._profitable_orders():
            self.transactor.sell(order)

    #  [wipn] logical update?
    #  this also needs to account for upward moving buys, so basically what I own sets a range
    #  and I buy above or below in intervals..?
    def _time_to_buy(self):
        return True # wipn remove
        #  return self._highest_buy_at() >= self.current_price
    
    def _profitable_orders(self):
        return Order.profitable(current_price=self.current_price)

    def _highest_buy_at(self):
        return Order.lowest_bought_at() - self.purchase_increment
