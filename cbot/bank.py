from cbot.coin import Coin

class Bank():
    coins = []

    def __init__(self, markets, client):
        self.client         = client
        self.usd_balance    = client.usd_balance()
        self.markets        = self._create_coins(markets)

    def balances(self, refresh=False):
        blncz = []
        for c in self.coins:
            if refresh:
                coin.update_balance()
            blncz.append({ 'name': c.market, 'balance': c.balance })
        return blncz

    def cash_out_value(self):
        return self.total_coin_values() + self.usd_balance

    def total_coin_values(self):
        total = 0.0
        for c in self.coins:
            total += float(c.worth())
        return total

    def _create_coins(self, markets):
        for market in markets:
            symbol = market.replace('-USD', '')
            self.coins.append(Coin(market, symbol, self.client))

