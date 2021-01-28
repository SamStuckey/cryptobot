#  [wipn] I think i'm getting rid of this in favor of putting quries on the client
class Query():
    def __init__(self, client):
        self.client = client

    def btc_price_in_usd(self):
        return self.client.ticker('BTC-USD')['price']

    def available_funds(self):
        return self.default_account #['available']


    #  def btc_holdings(self):
    #      return self.client.get_accounts[0]['available')
