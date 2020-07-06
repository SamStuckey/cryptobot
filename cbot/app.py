from cbot.client     import Client
from cbot.model      import Order
from cbot.query      import Query
from cbot.transactor import Transactor
from cbot.websocket  import Websocket
import time

class Cbot:
    def __init__(self):
        self.client     = Client()
        self.query      = Query(self.client)
        self.transactor = Transactor(self.client)
        self.ws         = Websocket()

    def __call__(self):
        try:
            self.ws.start()
            self._run()
        except:
            self.ws.close()

    def _run(self):
        pass
        #  self._process_transactions()
        #  run = True
        #  while run:
        #      self._process_transactions()
        #      self._wait()

    def _wait(self):
        time.sleep(sleep_time)
    
    def _process_transactions(self):
        self._sell_all_profitable_orders()
        #  if self._time_to_buy():
        #      self._place_market_buy()

    def _sell_all_profitable_orders(self):
        for order in self._profitable_orders():
            self.transactor.sell(order)

    def _time_to_buy(self):
        return self.lowest_buy_at - self.interval >= self.current_price
    
    def _profitable_orders(self):
        current_price = self.query.btc_price_in_usd()
        return Order.profitable(Order, current_price)

    def _buy_price(self):
        return self.lowest_buy_at - self.purchace_increment
