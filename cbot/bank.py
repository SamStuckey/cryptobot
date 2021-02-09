from cbot.coin import Coin

class Bank():
    coins = []

    def __init__(self, markets, client):
        self.client      = client
        self.usd_balance = client.usd_balance()
        self.markets     = self._create_coins(markets)

    def refresh_balances(self):
        self.usd_balance = client.usd_balance()
        for coin in self.coins:
            coins[coin] = client.coin_balance(coin)

    def balances(self):
        return coins

    def _create_coins(self, markets):
        for market in markets:
            self.coins.append(Coin(market, self.client))
