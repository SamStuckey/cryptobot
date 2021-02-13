from cbpro2 import PublicClient, AuthenticatedClient
from decouple import config

class CbClient:
    coinbase_key        = config('CB_API_PKEY')
    coinbase_secret     = config('CB_API_SKEY')
    coinbase_passphrase = config('CB_PASSPHRASE')
    usd_acc_num         = config('CB_USD_ACC_NUM')
    coin_acc_num        = config('CB_BTC_ACC_NUM')
    coin_acct_nums      = {}

    def __init__(self):
        self.pub_cli  = PublicClient()
        self.auth_cli = AuthenticatedClient(self.coinbase_key,
                                              self.coinbase_secret,
                                              self.coinbase_passphrase)

    def place_market_buy(self, amount, market):
        print('API CALL: place_market_buy')
        resp = self.auth_cli.place_market_order(product_id=market,
                                                side='buy',
                                                funds=amount)
        if resp.status_code == 200:
            print('success')
            return resp.json()
        else:
            self._log_failure(resp, 'place_market_buy')

    def place_market_sell(self, amount, market):
        print('API CALL: place_market_sell')
        resp = self.auth_cli.place_market_order(product_id=market,
                                                side='sell',
                                                size=amount)
        if resp.status_code == 200:
            print('success')
            return resp.json()
        else:
            self._log_failure(resp, 'place_market_sell')

    def get_order(self, order_id):
        print('API CALL: get_order')
        resp = self.auth_cli.get_order(order_id)
        if resp.status_code == 200:
            print('success')
            return resp.json() 
        else:
            self._log_failure(resp, 'get_order')

    def usd_balance(self):
        print('API CALL: usd_balance')
        resp = self.auth_cli.get_account(self.usd_acc_num)
        if resp.status_code == 200:
            print('success')
            return float(resp.json().get('balance'))
        else:
            self._log_failure(resp, 'usd_balance')

    def coin_price(self, coin):
        print('API CALL: coin_price: ' + coin.symbol)
        resp = self.pub_cli.get_product_ticker(coin.market)
        if resp.status_code == 200:
            print('success')
            return float(resp.json().get('price'))
        else:
            self._log_failure(resp, 'coin_price')

    def coin_balance(self, coin):
        acct_num = self.coin_acct_nums.get(coin.symbol)
        #  [wipn] might be able to get rid of this using named arguements
        if acct_num != None:
            return self._balance_by_number(acct_num)
        else:
            return self._balance_by_symbol(coin.symbol)

    def _balance_by_number(self, acct_num):
        print('API CALL: coin_balance by number')
        resp = self.auth_cli.get_account(acct_num)
        if resp.status_code == 200:
            print('success')
            return resp.json().get('balance')
        else:
            self._log_failure(resp, 'balance_by_number')

    def _balance_by_symbol(self, symbol):
        print('API CALL: coin_balance by symbol')
        resp = self.auth_cli.get_accounts()
        if resp.status_code == 200:
            print('success')
            account = self._pluck_account(symbol, resp.json())
            self._memoize_account_number(account)
            return account.get('balance')
        else:
            self._log_failure(resp, 'balance_by_symbol')

    def _log_failure(self, resp, source):
        print('!!!!!!!!!!!!! API ERROR !!!!!!!!!!!!!')
        print(str(source))
        print(resp.status_code)
        print(resp.json())
        print('--------------------------------------')

    def _pluck_account(self, symbol, accounts):
        symb = symbol.replace('-USD', '')
        for acc in accounts:
            if acc.get('currency') == symb:
                return acc

    def _memoize_account_number(self, account):
        self.coin_acct_nums[account.get('currency')] = account.get('id')
