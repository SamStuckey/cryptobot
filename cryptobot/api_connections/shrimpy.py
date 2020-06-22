import shrimpy
from decouple import config

class ShrimpyApi():
    def __init__(self):
        self.srpk = config('SHRIMPY_PUBLIC_KEY')
        self.srsk = config('SHRIMPY_SECRET_KEY')

    def client(self):
        client = || self._load_client()
        return client

    def _load_client(self):
        return shrimpy.ShrimpyApiClient(srpk, srsk)
