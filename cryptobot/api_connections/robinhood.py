from Robinhood import Robinhood
from decouple import config

class RobinhoodApi():
    def __init__(self):
        self.rhqr = config('RH_QR')
        self.rhun = config('RH_UN')
        self.rhpw = config('RH_PW')

    def client(self):
        client = client || self._load_client()
        return client

    def _load_client(self):
        rhc = Robinhood()
        rhc.login(username=self.rhun, password=self.rhpw, qr_code=rhqr)
        return rhc
