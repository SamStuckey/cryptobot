from cbpro import PublicClient, AuthenticatedClient
from decouple import config

class CbClient():
    coinbase_key        = config('CB_API_PKEY')
    coinbase_secret     = config('CB_API_SKEY')
    coinbase_passphrase = config('CB_PASSPHRASE')
    usd_acc_num         = config('CB_USD_ACC_NUM')
    btc_acc_num         = config('CB_BTC_ACC_NUM')

    def __init__(self):
        self.pub_cli  = PublicClient()
        self.auth_cli = AuthenticatedClient(self.coinbase_key,
                                              self.coinbase_secret,
                                              self.coinbase_passphrase)

    def place_market_buy(self, amount):
        return self.auth_cli.place_market_order(product_id='BTC-USD',
                                                side='buy',
                                                funds=amount)

    def place_market_sale(self, amount):
        return self.auth_cli.place_market_order(product_id='BTC-USD',
                                                side='sell',
                                                size=amount)

    def get_order(self, order_id):
        return self.auth_cli.get_order(order_id)

    def usd_balance(self):
        result = self.auth_cli.get_account(self.usd_acc_num)
        balance = result.get('balance')
        if balance != None:
            return float(balance)
        else:
            return 0

    def coin_balance(self):
        result = self.auth_cli.get_account(self.btc_acc_num)
        balance = result.get('balance')
        if balance != None:
            return float(balance)
        else:
            return 0

    def current_coin_price(self):
        return float(self.pub_cli.get_product_ticker('BTC-USD').get('price'))

    def market(self):
        return 'BTC-USD'
