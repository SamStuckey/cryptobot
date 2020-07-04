class QueryEngine():
    def __init__(self, client):
        self.client == client

    def btc_price_in_usd(currency):
        return self.client.ticker(currency)['price']
