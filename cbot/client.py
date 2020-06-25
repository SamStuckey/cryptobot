import cbpro
from Robinhood import Robinhood
from decouple import config

coinbase_key        = config('CB_API_PKEY')
coinbase_secret     = config('CB_API_SKEY')
coinbase_passphrase = config('CB_PASSPHRASE')
robinhood_qr        = config('RH_QR')
robinhood_username  = config('RH_UN')
robinhood_password  = config('RH_PW')

class CoinbaseClient():
    def __init__(self):
        self.pub_cli  = cbpro.PublicClient()
        self.auth_cli = cbpro.AuthenticatedClient(coinbase_key,
                                                  coinbase_secret,
                                                  coinbase_passphrase)

    def account(self):
        return self.auth_cli.get_accounts()

    def ticker(self, currency):
        return self.pub_cli.get_product_ticker(product_id=currency)

class RobinhoodClient():
    def __init__(self):
        self.client = Robinhood()
        self.client.login(username=robinghood_username,
                          password=robinhood_password,
                          qr_code=robinhood_qr)

    def account(self):
        self.client
