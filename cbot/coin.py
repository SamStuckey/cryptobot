class Coin:
    min_price = 35

    def __init__(self, market, client):
        self.client   = client
        self.market   = market
        self.balance  = self.client.coin_balance(self.market)
        self.price    = self.client.coin_price(self.market)

    def worth(self):
        return self.balance * self.price

    def update_balance(self):
        self.balance = self.client.coin_balance(self.market)
        return self.balance

    def update_price(self):
        self.price = self.client.coin_price(self.market)
        return self.price

    def buy(self, amount):
        return self.client.place_market_buy(amount, self.market)

    def sell(self, amount):
        return self.client.place_market_sale(amount, self.market)

