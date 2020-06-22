from cryptobot.api_connections import shrimpy
from cryptobot.api_connections.coinbase import CoinbaseApi
from cryptobot.api_connections.robinhood import RobinhoodApi
from decouple import config
import time

cb_client = CoinbaseApi()
buy_threshold = 9400

class Cryptobot:

    def __init__(self):
        self.buy_threshold = config('BUY_THRESHOLD')
        self.buy_interval  = config('BUY_INTERVAL')
        self.sell_interval = config('BUY_INTERVAL')

    def _coinbase(self):
        coinbase = coinbase or CoinbaseApi().client
        return coinbase

    def _robinhood(self):
        robinhood = coinbase or RobinhoodApi().client
        return robinhood

    def run(self):
        self.last_limit = self._coinbase.get_current_btc_price()
        while True:
            self._process_transactions()
            self._wait()

    def _wait(self):
        time.sleep(self.buy_interval)

    def _set_next_limit_buy():
        """ 
            - create a record of:
                - price of BTC
                - amount of BTC
                - value in USD
                - price to sell at
            - order USD amount at next BTC decrement
        """
        print('you')

    def _make_available_sales(self):
        """
            - load order records where sell_at <= current_price 
        """
        for sale in self.sales:
            self._attempt_sale(sale)


    def _falling(self):
        self._current_price <= self._last_order_price()

    def _process_transactions(self):
        """
            Get current price and 
            When do i set a limit buy?
                - i could just set them all the way down?
        """
        if self._falling():
            _set_next_limit_buy()
        else:
            self._cancel_next_limit_buy()
            self._make_available_sales()

    def _set_limit_buys()
        # the 'instrument' is the STOCK i want to buy...
            # TBD: what does this mean for bitcoin?
        # index of instruments here: https://api.robinhood.com/instruments/
        # instrument_url  https://api.robinhood.com/instruments/<instrument hash>
        robinhood.place_limit_buy_order(instrument_URL=self,
                                        symbol=self._symbol(),
                                        time_in_force=self._time_in_force(),
                                        price=self._price(),
                                        quantity=self._quantity())

    def _cancel_next_limit_buy(self):
        print('canceling limit buys')

    def _buy(self):
        return self._current_price <= self.last_limit

    def _current_price(self):
        return cb_client.get_current_btc_price()


    def _attempt_sale(self, sale):
        if current_price <= sale.sell_at_price:
            sale.execute()
