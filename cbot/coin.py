class Coin:
    min_price = 35

    def __init__(self, market, symbol, client):
        self.client   = client
        self.symbol   = symbol
        self.market   = market
        self.balance  = float(self.client.coin_balance(self))
        self.price    = float(self.client.coin_price(self))

    def worth(self):
        return self.balance * float(self.price)

    def update_balance(self):
        self.balance = self.client.coin_balance(self)
        return self.balance

    def update_price(self):
        self.price = self.client.coin_price(self)
        return self.price

    def buy(self, amount):
        return self.client.place_market_buy(amount, self.market)

    def sell(self, amount):
        return self.client.place_market_sell(amount, self.market)
