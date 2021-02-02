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
        resp = self.auth_cli.place_market_order(product_id='BTC-USD',
                                                side='buy',
                                                funds=amount)
        return self._qualified(resp)

    def place_market_sale(self, amount):
        resp = self.auth_cli.place_market_order(product_id='BTC-USD',
                                                side='sell',
                                                size=amount)
        return self._qualified(resp)

    def get_order(self, order_id):
        resp = self.auth_cli.get_order(order_id)
        return self._qualified(resp)

    def usd_balance(self):
        resp = self.auth_cli.get_account(self.usd_acc_num)
        qualified = self._qualified(resp)
        if qualified['success']:
            return float(resp.get('balance'))

    def coin_balance(self):
        resp = self.auth_cli.get_account(self.usd_acc_num)
        qualified = self._qualified(resp)
        if qualified['success']:
            return float(resp.get('balance'))

    def current_coin_price(self):
        resp = self.pub_cli.get_product_ticker('BTC-USD')
        qualified = self._qualified(resp)
        if qualified['success']:
            return float(resp.get('price'))

    def market(self):
        return 'BTC-USD'

    #  [wipn] START HERE - continue trying to decorate the client response with
    #  a success indicator
    def _qualified(self, resp):
        resp['success'] = resp.get('error') == None
        return resp
