import cbpro, time
from cbot.app import Cbot

class Websocket(cbpro.WebsocketClient):
    cbot = Cbot()
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD"]
        self.channels = ["ticker"]

    def on_message(self, msg):
        self.cbot(msg.get('price'))
