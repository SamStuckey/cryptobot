from coinbase.wallet.client import Client
from decouple import config

cbk = config('CB_API_PKEY')
cbs = config('CB_API_SKEY')

def load_coinbase_client():
    return Client(cbk, cbs)
