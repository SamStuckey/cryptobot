import shrimpy
import os

public_key = os.getenv['SHRIPY_PUBLIC_KEY']
secret_key = os.getenv['SHRIPY_SECRET_KEY']
client = shrimpy.ShrimpyApiClient(public_key, secret_key)
ticker = client.get_ticker('bittrex')
