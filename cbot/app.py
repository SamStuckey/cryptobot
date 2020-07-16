from cbot.client     import Client
from cbot.model      import Order
from cbot.query      import Query
from cbot.transactor import Transactor

interval = 10
class Cbot:
    def __init__(self):
        self.client     = Client()
        self.query      = Query(self.client)
        self.transactor = Transactor(self.client)

    def __call__(self, price):
        return self._lowest_buy_at()

    #  [wipn] keep
    #  def __call__(self, price):
    #      if price is not None:
    #          self.price = price
    #          self._sell_all_profitable_orders()
    #      if self._time_to_buy():
    #          self._place_market_buy()

    def _sell_all_profitable_orders(self):
        for order in self._profitable_orders():
            self.transactor.sell(order)

    def _time_to_buy(self):
        return self._lowest_buy_at >= self.current_price
    
    #  [wipn] START HERE - should be working up to here, just find out how to
    #  define an order model with the 'profitable' scope and do this lookup
    def _profitable_orders(self):
        return Order.profitable(current_price=self.price)

    def _buy_price(self):
        return self.lowest_buy_at - self.purchace_increment

    def _lowest_buy_at(self):
        return Order.lowest_bought_at() #- interval
