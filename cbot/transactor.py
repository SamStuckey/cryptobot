from cbot.model import Order

currency = 'BTC-USD'

class Transactor():
    def __init__(self, client):
        self.client = client

    #  [wipn] dry run
    def dry_run_buy(self, amount):
        pass
        #  result = {
        #              purchase_rate:
        #          }
        #  return Order.create_purchase(result)

    def dry_run_sale(self, amount):
        pass
        #  result = {
        #              purchase_rate:
        #          }
        #  return Order.create_purchase(result)

    def market_buy(self, amount):
        result = self.client.place_market_order(amount)
        return Order.create_purchase(result)

    def market_sale(self, order):
        pass
        #  [wipn] don't know if 'sell' is right
        #  response = self.client.sell({'amount' => order.btc_quantity,
        #                  'currency' => 'BTC',
        #                  'payment_method' => self._payment()})
        #  order.sold_at_rate = response.??
