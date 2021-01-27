import cbpro, time
from cbot.app import Cbot

class Websocket(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD"]
        self.channels = ["ticker"]

    def on_message(self, msg):
        price = msg.get('price')
        print("received price: ", price)
        Cbot()(price)
