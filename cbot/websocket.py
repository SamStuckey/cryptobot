import cbpro, time
from cbot.app import Cbot


class Websocket(cbpro.WebsocketClient):
    app_runs = 0

    def on_open(self):
        self.cbot = Cbot()
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD"]
        self.channels = ["ticker"]

    def on_message(self, msg):
        if self.app_runs > 2000000000:
            print('reseting after 2000000000th run')
            self.cbot = Cbot()
            self.app_runs = 0
        else:
            self.cbot(msg.get('price'), self.app_runs)
            self.app_runs += 1

