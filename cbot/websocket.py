import cbpro, time

class Websocket(cbpro.WebsocketClient):
    def on_open(self):
        print("opening connection")
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD"]
        self.channels = ["ticker"]

    #  [wipn] how the hell do i leverage this to trigger events at the top level?
    def on_message(self, msg):
        print(msg)
        price = msg['price']

    def on_close(self):
        pass
