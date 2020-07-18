from cbot.client     import Client
from cbot.model      import Order
from cbot.query      import Query
from cbot.transactor import Transactor

class Cbot:
    btc_purchase_increment = 10
    usd_buy_amount         = 100
    btc_required_increase  = 50

    def __init__(self):
        self.client     = Client()
        self.query      = Query(self.client)
        self.transactor = Transactor(self.client)

    def __call__(self, price):
        if price is not None:
            self.price = price
            #  self._execute_sales()
            self._execute_purchase()

    # should never run, but worth keeping as a fail safe.  update logic to
    # make sure i'm not trying to 'double sell' an order that is already set
    # for limit sale.
    def _execute_sales(self):
        self._sell_all_profitable_orders()

    def _execute_purchase(self):
        if self._time_to_buy():
            new_order = self._place_market_buy()
            self._set_limit_sale(new_order)
            print('purchased: ', new_order)

    def _set_limit_sale(self, order):
        sell_price = new_order.buy_btc_val + self.btc_required_increase
        self.transactor.place_limit_sale(new_order, sell_price=sell_price)

    def _place_market_buy(self):
        result = self.transactor.market_buy(self.buy_amount)
        order = Order.build_from_transaction(result)
        return order

    #  [wipn] this probably doesn't need to happen, if i just set market sell orders
    #  when i buy
    def _sell_all_profitable_orders(self):
        for order in self._profitable_orders():
            self.transactor.sell(order)

    #  [wipn] logical update?
    #  this also needs to account for upward moving buys, so basically what I own sets a range
    #  and I buy above or below in intervals..?
    def _time_to_buy(self):
        return self._highest_buy_at() >= self.current_price
    
    def _profitable_orders(self):
        return Order.profitable(current_price=self.current_price)

    def _highest_buy_at(self):
        return Order.lowest_bought_at() - self.purchase_increment
