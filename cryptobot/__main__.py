#  [wipn] KEEP
#  from .app.cryptobot import Cryptobot
#  Cryptobot.run()

#  [wipn] TEST ONLY
from cryptobot.api_connections.coinbase import CoinbaseApi
cb_api = CoinbaseApi()
price = cb_api.get_current_btc_price()
print(price)
