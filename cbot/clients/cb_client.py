from cbpro2 import PublicClient, AuthenticatedClient
from decouple import config

class CbClient:
    coinbase_key        = config('CB_API_PKEY')
    coinbase_secret     = config('CB_API_SKEY')
    coinbase_passphrase = config('CB_PASSPHRASE')
    usd_acc_num         = config('CB_USD_ACC_NUM')
    coin_acc_num        = config('CB_BTC_ACC_NUM')
    market              = 'BTC-USD' # config('MARKET')

    def __init__(self):
        self.pub_cli  = PublicClient()
        self.auth_cli = AuthenticatedClient(self.coinbase_key,
                                              self.coinbase_secret,
                                              self.coinbase_passphrase)

    def place_market_buy(self, amount, market):
        resp = self.auth_cli.place_market_order(product_id=market,
                                                side='buy',
                                                funds=amount)
        if resp.status_code == 200:
            return resp.json()
        else:
            self._log_failure(resp, 'place_market_buy')

    def place_market_sale(self, amount, market):
        resp = self.auth_cli.place_market_order(product_id=market,
                                                side='sell',
                                                size=amount)
        if resp.status_code == 200:
            return resp.json()
        else:
            self._log_failure(resp, 'place_market_sale')

    def get_order(self, order_id):
        resp = self.auth_cli.get_order(order_id)
        if resp.status_code == 200:
            print('we made it')
            return resp.json() 
        else:
            self._log_failure(resp, 'get_order')
 

    def usd_balance(self):
        resp = self.auth_cli.get_account(self.usd_acc_num)
        if resp.status_code == 200:
            return float(resp.json().get('balance'))
        else:
            self._log_failure(resp, 'usd_balance')

    def coin_balance(self, symbol):
        resp = self.auth_cli.get_account(symbol)
        if resp.status_code == 200:
            return float(resp.json().get('balance'))
        else:
            self._log_failure(resp, 'coin_balance')

    def coin_price(self, market):
        resp = self.pub_cli.get_product_ticker(market)
        if resp.status_code == 200:
            return float(resp.json().get('price'))
        else:
            self._log_failure(resp, 'current_coin_price')

    def _log_failure(self, resp, source):
        print('!!!!!!!!!!!!! API ERROR !!!!!!!!!!!!!')
        print(source)
        print(resp.status_code)
        print(resp.json())

    def market(self):
        return self.market
