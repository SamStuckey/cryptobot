from cbot.model import Order

currency = 'BTC-USD'

class Transactor():
    def __init__(self, client):
        self.client = client

    def market_buy(self, amount):
        result = self.client.place_market_order(amount)
        return Order.create_purchase(result)

    def buy(self, orders):
        pass
        #  self.client.buy({'amount' => order.btc_quantity,
        #                  'currency' => 'BTC',
        #                  'payment_method' => self._payment()

    def sell(self, order):
        pass
        #  self.client.sell({'amount' => order.btc_quantity,
        #                  'currency' => 'BTC',
        #                  'payment_method' => self._payment()})

    def _payment(self):
        pass
        #  self.client.payment_methods.first
