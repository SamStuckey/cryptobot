class Query():
    def __init__(self, client):
        self.client = client

    def btc_price_in_usd(self):
        return self.client.ticker('BTC-USD')['price']
