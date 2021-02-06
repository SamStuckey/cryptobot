from cbot.clients.cb_client import CbClient

class Bank():
    coins = []

    def __init__(self, markets, client):
        self.client      = client
        self.usd_balance = client.usd_balance()
        self.markets     = self._create_coins(markets)

    def refresh_balances(self):
        self.usd_balance = client.usd_balance()
        for coin in coins:
            coins[coin] = client.coin_balance(coin)

    def balances(self):
        return coins

    def _create_coins(self, markets):
        for market in markets:
            coins.append(Coin(market, client))
