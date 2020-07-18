currency = 'BTC-USD'

class Transactor():
    def __init__(self, client):
        self.client = client

    def market_buy(self, amount):
        result = auth_client.place_market_order(product_id='BTC-USD', 
                                   side='buy', 
                                   funds='100.00')
        return result

    def buy(self, orders):
        #  pass
        self.client.buy({'amount' => order.buy_btc_val,
                        'currency' => 'BTC',
                        'payment_method' => self._payment()

    def sell(self, order):
        pass
        #  self.client.sell({'amount' => order.buy_btc_val,
        #                  'currency' => 'BTC',
        #                  'payment_method' => self._payment()})

    def _payment(self):
        self.client.payment_methods.first
