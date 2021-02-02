import cbpro, time
import datetime
from cbot.app import Cbot
from decouple import config

class Websocket(cbpro.WebsocketClient):
    app_runs = 0

    def on_open(self):
        self.cbot     = Cbot()
        self.last_run = datetime.datetime.now()
        self.url      = config('API_URL')
        self.products = config('MARKET')
        self.channels = ["ticker"]

    def on_message(self, msg):
        if self._sufficently_throttled():
            self._load_and_fire(msg)

    def _sufficently_throttled(self):
        return self.last_run + datetime.timedelta(0, 3) < datetime.datetime.now()

    def _load_and_fire(self, msg):
        if self.app_runs > 2000000000:
            print('reseting after 2000000000th run')
            self.cbot = Cbot()
            self.app_runs = 0
        else:
            self.cbot(msg.get('price'), self.app_runs)
            self.app_runs += 1
            self.last_run = datetime.datetime.now()
