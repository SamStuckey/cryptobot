from cryptobot.api_connections import shrimpy
from cryptobot.api_connections.coinbase import CoinbaseApi
from cryptobot.api_connections.robinhood import RobinhoodApi
from decouple import config
import time

class Cryptobot:
    def __init__(self):
        self.interval  = config('INTERVAL')
        #  [wipn] deterimine what unit this uses and set it in the .env
        self.time_in_force  = config('TIME_IN_FORCE')

    def __call__(self):
        while True:
            self.market_price = self._get_market_price()
            self._process_transactions()
            self._wait()

    # refactor into singleton
    def _coinbase(self):
        coinbase = coinbase or CoinbaseApi().client
        return coinbase

    # refactor into singleton
    def _robinhood(self):
        robinhood = coinbase or RobinhoodApi().client
        return robinhood

    def _wait(self):
        time.sleep(self.buy_interval)
        return True

    def _process_transactions(self):
        self._sell_all_profitable_orders()
        if self._time_to_buy():
            self._place_market_buy()

    def _sell_all_profitable_orders(self):
        for order in self._profitable_orders()
            order.sell()

    def _profitable_orders(self):
        #  [wipn] psuedo code - make this work
        #  orders.where(purchased_at + self.interval <= self.market_price)

    def _time_to_buy(self):
        #  [wipn] make this work
        return self.lowest_buy_at - self.interval >= self.current_price

    def _place_market_buy(self):
        # index of instruments here: https://api.robinhood.com/instruments/
        # instrument_url  https://api.robinhood.com/instruments/<instrument hash>
        robinhood.place_limit_buy_order(instrument_URL='wipn',
                                        symbol='BTC',
                                        time_in_force=self.time_in_force,
                                        price=self._buy_price(),
                                        quantity=quantity)
        self.lowest_buy_at = self._buy_price()
        return True

    def _buy_price(self):
        return self.lowest_buy_at - self._interval

    def _get_market_price(self):
        return cb_client.get_current_btc_price()
