from cbpro2 import PublicClient, AuthenticatedClient
from decouple import config

class CbClient:
    coinbase_key        = config('CB_API_PKEY')
    coinbase_secret     = config('CB_API_SKEY')
    coinbase_passphrase = config('CB_PASSPHRASE')
    usd_acc_num         = config('CB_USD_ACC_NUM')
    coin_acc_num        = config('CB_BTC_ACC_NUM')

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
        acct_num = self.acct_nums[symbol]
        if acct_num != None:
            return self._balance_by_number(acct_num)
        else:
            return self._balance_by_symbol(symbol)

    def _balance_by_number(self, acct_num):
        resp = self.auth_cli.get_account(acct_num)
        if resp.status_code == 200:
            return self._get_account_for(symbol, resp)
        else:
            self._log_failure(resp, 'coin_balance')

    def _balance_by_symbol(self, symbol):
        resp = self.auth_cli.get_accounts()
        if resp.status_code == 200:
            account = self._pluck_account(symbol, resp.json())
            return self._get_account_for(symbol, resp)
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
        print('FAILED CALL: ' + str(source))
        print(resp.status_code)
        print(resp.json())

    def _pluck_account(self, accounts):
        for acc in accounts:
            if acc.get('symbol') == symbol:
                account = acc
                break
        return account
