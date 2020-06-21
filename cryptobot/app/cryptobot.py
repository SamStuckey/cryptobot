from cryptobot.api_connections import shrimpy
from cryptobot.api_connections.coinbase import CoinbaseApi
from pynput.keyboard import Key, Listener
from decouple import config
import time

cb_client = CoinbaseApi()
buy_threshold = 9400

"""
on load
set buys in increments of -10 value down to ... what?
    - each has a sell at price.
    - sell at just triggers automatically every 10 seconds.

selling is easy
how / when do i buy?

either preset
or
check price each 10 seconds and buy if down.  That   the problem is, do i risk missing out on several buys on the way down?  
START HERE - figure out my buy strategy

    - resale profit margin should be set higher as buy price goes down
    - buy amount should increase as price goes down
    1. preset buys below a certain threshold at run time.
        - need to be re-ordered once the price goes back above this point.
        - only place orders lower than current price
    2. check in every 10 seconds.
        - if price is below buy threshold then buy
            - how much do i buy?  should it change based on the price change?

"""

class Cryptobot:
    interval = 10

    def __init__(self):
        self.do_run        = True
        self.last_limit    = cb_client.get_current_btc_price()

    def run(self):
        while True:
            self._process_transactions()
            time.sleep(interval)

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

    def _cancel_next_limit_buy(self):
        print('canceling limit buys')

    def _buy(self):
        return self._current_price <= self.last_limit

    def _current_price(self):
        return cb_client.get_current_btc_price()


    def _attempt_sale(self, sale):
        if current_price <= sale.sell_at_price:
            sale.execute()
