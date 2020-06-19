from .api_connections import shrimpy
from .api_connections.coinbase import CoinbaseApi

def get_current_btc_price():

interval = 10
#  [wipn] START HERE - implement this 'get starting price' function
#  implement buy logic
starting_price = get_current_btc_price






cb_api = CoinbaseApi()
print(cb_api.balance_usd())
print(cb_api.accounts)
