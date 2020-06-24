from cryptobot.api_clients.coinbase import load_auth_client, load_public_client

class CoinbaseApi():
    def __init__(self):
        self.auth_client = load_auth_client()
        self.client = load_public_client()

    def accounts(self):
       self.auth_client.get_accounts()

    def get_price_for(self, symb):
        for currency in self.client.get_currencies():
            if currency['id'] == 'BTC':
                return currency

    def balance_usd(self):
        for acc in self.accounts:
             if acc['currency'] == 'USD':
                 return acc['balance']

    def currencies(self):
        return self.client.currencies()
