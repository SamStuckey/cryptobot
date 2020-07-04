from cbot.client     import Client
from cbot.model      import Order
from cbot.query      import QueryEngine
from cbot.transactor import TransactionEngine
import time

sleep_time = 1
currency = 'BTC-USD'

class Cbot:

    def __init__(self, interval, time_in_force):
        self.interval      = interval
        self.time_in_force = time_in_force
        self.client        = Client()
        self.query_engine  = QueryEngine(self.client)
        self.transactor    = TransactionEngine(self.client)

    def __call__(self):
        run = True
        while run:
            self.market_price = btc_price_in_usd(currency)
            print(self.market_price)
            run = False
            #  self._process_transactions()
            #  self._wait()

    def _wait(self):
        time.sleep(sleep_time)
    
    def _process_transactions(self):
        self._sell_all_profitable_orders()
        if self._time_to_buy():
            self._place_market_buy()

    #  [wipn] hook me up to a DB
    def _sell_all_profitable_orders(self):
        for order in self._profitable_orders():
            sell(order)

    def _time_to_buy(self):
        #  [wipn] make this work
        return self.lowest_buy_at - self.interval >= self.current_price
    #
    def _profitable_orders(self):
        pass
        #  [wipn] psuedo code - make this work
        #  orders.where(purchased_at + self.interval <= self.market_price)


    def _place_market_buy(self):
        # index of instruments here: https://api.robinhood.com/instruments/
        # instrument_url  https://api.robinhood.com/instruments/<instrument hash>
        #  [wipn] START HERE - figure out what an instrument is, how to get it, and place an order
        #  e.g. - each stock seems to have one instrument, so i just need to figure out 
        #   the symbol is for bitcoin
        #  print(self.rh_client.instruments('MSFT')[0]['url'])
        self.rh_client.place_market_order(instrument_URL='wipn',
                                        symbol='BTC',
                                        time_in_force=self.time_in_force,
                                        price=self._buy_price(),
                                        quantity=quantity)
        #  auth_client.place_market_order(product_id='BTC-USD',
        #                         side='buy',
        #                         funds='100.00')
        self.lowest_buy_at = self._buy_price()
        return True
    #
    #  def _buy_price(self):
    #      return self.lowest_buy_at - self._interval
    #
    def _get_market_price(self):
        return self.cb_client.get_buy_price(currency_pair = 'BTC-USD')
