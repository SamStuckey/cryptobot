import cbpro
from decouple import config

cbk = config('CB_API_PKEY')
cbs = config('CB_API_SKEY')
cbp = config('CB_PASSPHRASE')

def load_auth_client():
    return cbpro.AuthenticatedClient(cbk, cbs, cbp)

def load_public_client():
    return cbpro.PublicClient()

