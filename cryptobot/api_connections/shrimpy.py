#  import shrimpy
#  from decouple import config
#
#  shrimpy_public_key = config('SHRIMPY_PUBLIC_KEY')
#  shrimpy_secret_key = config('SHRIMPY_SECRET_KEY')
#  client = shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_secret_key)
import shrimpy
from decouple import config

def load_client():
    shrimpy_public_key = config('SHRIMPY_PUBLIC_KEY')
    shrimpy_secret_key = config('SHRIMPY_SECRET_KEY')

    return  shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_secret_key)

class ShrimpyApi():
    def __init__(self):
        self.client = load_client()
