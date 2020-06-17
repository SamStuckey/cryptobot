import shrimpy
from decouple import config

#  Shrimpy setup
shrimpy_public_key = config('SHRIMPY_PUBLIC_KEY')
shrimpy_secret_key = config('SHRIMPY_SECRET_KEY')
client = shrimpy.ShrimpyApiClient(public_key, secret_key)
ticker = client.get_ticker('bittrex')
print(ticker)

#  coinbase setup
# START HERE - connnect to my account and get the balance
cb_sandbox_url = 'https://api-public.sandbox.pro.coinbase.com'
cb_public_key = config('COINBASE_PUBLIC_KEY')
cb_secret_key = config('COINBAS_SECRET_KEY')

