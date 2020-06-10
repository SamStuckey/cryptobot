import shrimpy
from decouple import config
import os

public_key = config('SHRIMPY_PUBLIC_KEY')
secret_key = config('SHRIMPY_SECRET_KEY')
print(secret_key)
print(public_key)

print('ok workinng')

#  client = shrimpy.ShrimpyApiClient(public_key, secret_key)
#  ticker = client.get_ticker('bittrex')
