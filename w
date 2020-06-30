import cbpro
from Robinhood import Robinhood
from decouple import config

coinbase_key        = config('CB_API_PKEY')
coinbase_secret     = config('CB_API_SKEY')
coinbase_passphrase = config('CB_PASSPHRASE')
robinhood_qr        = config('RH_QR')
robinhood_username  = config('RH_UN')
robinhood_password  = config('RH_PW')

cb_pub_cli  = cbpro.PublicClient()
cb_auth_cli = cbpro.AuthenticatedClient(coinbase_key,
                                      coinbase_secret,
                                      coinbase_passphrase)

rh_client = Robinhood()
rh_client.login(username=robinhood_username,
              password=robinhood_password,
              qr_code=robinhood_qr)

class CoinbaseClient():
    def account(self):
        return cb_auth_cli.get_accounts()

    def ticker(self, currency):
        return cb_pub_cli.get_product_ticker(product_id=currency)

class RobinhoodClient():
    def account(self):
        return rh_client.get_accounts()

    def buy(self):
        return rh_client.place_market_buy_order()
