from cbot.client     import Client
from cbot.model      import Order
from cbot.query      import Query
from cbot.transactor import Transactor

class Cbot:
    def __init__(self):
        self.client     = Client()
        self.query      = Query(self.client)
        self.transactor = Transactor(self.client)

    def __call__(self, price):
        self.price = price
        self._sell_all_profitable_orders()

        if self._time_to_buy():
            self._place_market_buy()

    def _sell_all_profitable_orders(self):
        for order in self._profitable_orders():
            self.transactor.sell(order)

    def _time_to_buy(self):
        return self.lowest_buy_at - self.interval >= self.current_price
    
    #  [wipn] START HERE - should be working up to here, just find out how to
    #  define an order model with the 'profitable' scope and do this lookup
    def _profitable_orders(self):
        return Order.profitable(Order, self.price)

    def _buy_price(self):
        return self.lowest_buy_at - self.purchace_increment
