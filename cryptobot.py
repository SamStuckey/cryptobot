#  import shrimpy
from decouple import config
import os

public_key = config['SHRIPY_PUBLIC_KEY']
secret_key = config['SHRIPY_SECRET_KEY']
print public_key
print secret_key_key
#  client = shrimpy.ShrimpyApiClient(public_key, secret_key)
#  ticker = client.get_ticker('bittrex')
