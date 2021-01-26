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
        self.uninitialized = True
        self.client        = Client()
        self.transactor    = Transactor(self.client)

    def __call__(self, price):
        if self.uninitialized:
            self.uninitialized = False
            #  self.action_ceiling = price +
            #  self.action_floor = price -

        if price is not None:
            self.price = price

            #  [wipn] START HERE - polish the algorythm and test sales
            # if price is 10 greater than last, buy
            #  if price is 10 less than last, sell all profitable
            # profitable means selling recoups original  Plus cost of selling

            #  [wipn] not tested yet
            #  self._execute_sales()

            #  [wipn] this works in cb and successfully writes to my db
            #  self._execute_purchase()

            #  self._update_pending_orders()

    def _execute_sales(self):
        self._sell_all_profitable_orders()

    def _update_pending_orders(self):
        for order in Order.pending():
            cb_record = self.client.get_order(order.external_id)

            if self._needs_update(cb_record.get('status'), order.status):
                order.execute_purchase(cb_record)

    def _needs_update(self, ext_status, int_status):
        return ext_status != 'pending' and ext_status != int_status

    def _execute_purchase(self):
        if self._time_to_buy():
            self.transactor.market_buy(self.usd_buy_amount)

    #  def _set_limit_sale(self, order):
    #      sell_price = new_order.btc_quantity + self.btc_required_increase
    #      self.transactor.place_limit_sale(new_order, sell_price=sell_price)

    def _sell_all_profitable_orders(self):
        for order in self._profitable_orders():
            self.transactor.sell(order)

    def _time_to_buy(self):
        return True
        #  return self._highest_buy_at() >= self.current_price
    
    def _profitable_orders(self):
        return Order.profitable(current_price=self.current_price)

    def _highest_buy_at(self):
        return Order.lowest_bought_at() - self.purchase_increment
