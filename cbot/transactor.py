currency = 'BTC-USD'

class Transactor():
    def __init__(self, client):
        self.client = client

    def buy(self, orders):
        pass
        #  self.client.buy({'amount' => order.buy_btc_val,
        #                  'currency' => 'BTC',
        #                  'payment_method' => self._payment()

    def sell(self, order):
        pass
        #  self.client.sell({'amount' => order.buy_btc_val,
        #                  'currency' => 'BTC',
        #                  'payment_method' => self._payment()})

    def _payment(self):
        self.client.payment_methods.first
