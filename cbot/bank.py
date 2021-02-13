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
            coin.update_balance()

    def balances(self, refresh=False):
        blncz = []
        for c in coins:
            if refresh:
                coin.update_balance()
            b.append({ 'name': c.market, 'balance': c.balance })
        return blncz

    def _create_coins(self, markets):
        for market in markets:
            symbol = market.replace('-USD', '')
            self.coins.append(Coin(market, symbol, self.client))
