import shrimpy
from decouple import config
import os

public_key = config['SHRIMPY_PUBLIC_KEY']
secret_key = os.getenv['SHRIMPY_SECRET_KEY']
print(public_key)
print(secret_key_key)
#  client = shrimpy.ShrimpyApiClient(public_key, secret_key)
#  ticker = client.get_ticker('bittrex')
