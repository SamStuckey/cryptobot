#  import cbpro
from coinbase.wallet.client import Client
from decouple import config

cbk = config('CB_API_PKEY')
cbs = config('CB_API_SKEY')
#  cbp = config('CB_PASSPHRASE')

def load_auth_client():
    #  return cbpro.AuthenticatedClient(cbk, cbs, cbp)
    return Client(cbk, cbs)

def load_public_client():
    return cbpro.PublicClient()
