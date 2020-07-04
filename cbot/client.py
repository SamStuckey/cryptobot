import cbpro
from Robinhood import Robinhood
from decouple import config

coinbase_key        = config('CB_API_PKEY')
coinbase_secret     = config('CB_API_SKEY')
coinbase_passphrase = config('CB_PASSPHRASE')

cb_pub_cli  = cbpro.PublicClient()
cb_auth_cli = cbpro.AuthenticatedClient(coinbase_key,
                                      coinbase_secret,
                                      coinbase_passphrase)

class Client():
    def account(self):
        return cb_auth_cli.get_accounts()

    def ticker(self, currency):
        return cb_pub_cli.get_product_ticker(product_id=currency)
