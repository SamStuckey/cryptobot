import cbpro
from decouple import config

class CoinbaseApi():
    cb_sandbox_url = 'https://api-public.sandbox.pro.coinbase.com'
    cb_prod_url = 'https://api-public.sandbox.pro.coinbase.com'
    cb_key = config('CB_API_PKEY')
    cb_secret = config('CB_API_SKEY')
    cb_phrase = config('CB_PASSPHRASE')
    auth_client = cbpro.AuthenticatedClient(cb_key, cb_secret, cb_phrase)

    def __init__(self):
        self.accounts = self.auth_client.get_accounts()

    def accounts(self):
        return self.accounts

    def balance_usd(self):
        global result
        for acc in self.accounts:
             if acc['currency'] == 'USD':
                 return acc['balance']
