#  [wipn] KEEP
#  from .app.cryptobot import Cryptobot
#  cb = Cryptobot()
#  cb()

#  [wipn] TEST ONLY - working except not for price
#  from cryptobot.api_connections.coinbase import CoinbaseApi
#  cb_api = CoinbaseApi()
#  price = cb_api.get_price_for('BTC')
#  print(price)

from coinbase.wallet.client import Client
from decouple import config

cbk = config('CB_API_PKEY')
cbs = config('CB_API_SKEY')
client = Client(cbk, cbs)
price = client.get_buy_price(currency_pair = 'BTC-USD')
print(price)
