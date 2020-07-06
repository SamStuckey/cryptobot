currency = 'BTC-USD'
variable_quantity = 10
profit_requirement = 10 # need to figure this out with the fees and stuff

class Transactor():
    def __init__(self, client):
        self.client = client

    def buy(self, orders):
        print('buying: ', orders)
        pass

    def sell(self, order):
        print('selling: ', order)
        self.client.sell(order)
