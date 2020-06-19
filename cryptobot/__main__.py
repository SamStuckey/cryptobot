from .api_connections import shrimpy
from .api_connections.coinbase import CoinbaseApi
from pynput.keyboard import Key, Listener
import time

class Cryptobot:
    interval = 10
    last_limit = get_current_btc_price()
    set_next_limit_buy()

    def __init__(self):

    def get_current_btc_price():
        print('hey')

    def run():
        while run:
            current_price = get_current_btc_price()
            if current_price <= last_limit:
                set_next_limit_buy()
            else
                cancel_next_limit_buy()
                make_available_sales
            time.sleep(interval)

    def make_available_sales(self):
        for sale in self.sales:
            attempt_sale(sale)

    def attempt_sale(self, sale):
        if current_price <= sale.sell_at_price:
            sale.execute()

    cb_api = CoinbaseApi()
    print(cb_api.balance_usd())
    print(cb_api.accounts)
