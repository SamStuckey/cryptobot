#  bye = Buy(666)
#  bye.print_it()


#  Shrimpy setup
#  shrimpy_public_key = config('SHRIMPY_PUBLIC_KEY')
#  shrimpy_secret_key = config('SHRIMPY_SECRET_KEY')
#  client = shrimpy.ShrimpyApiClient(public_key, secret_key)
#  ticker = client.get_ticker('bittrex')
#  print(ticker)

#  coinbase setup
import shrimpy
from decouple import config
import cbpro

cb_sandbox_url = 'https://api-public.sandbox.pro.coinbase.com'
cb_prod_url = 'https://api-public.sandbox.pro.coinbase.com'
cb_key = config('CB_API_PKEY')
cb_secret = config('CB_API_SKEY')
cb_phrase = config('CB_PASSPHRASE')

auth_client = cbpro.AuthenticatedClient(cb_key, cb_secret, cb_phrase)
accounts = auth_client.get_accounts()

for acc in accounts:
    if acc['currency'] == 'USD':
        print(acc['balance'])
