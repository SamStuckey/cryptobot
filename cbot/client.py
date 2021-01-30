import cbpro
from decouple import config

coinbase_key        = config('CB_API_PKEY')
coinbase_secret     = config('CB_API_SKEY')
coinbase_passphrase = config('CB_PASSPHRASE')
cb_usd_acc_num      = config('CB_USD_ACC_NUM')
cb_btc_acc_num      = config('CB_BTC_ACC_NUM')

cb_pub_cli  = cbpro.PublicClient()
cb_auth_cli = cbpro.AuthenticatedClient(coinbase_key,
                                      coinbase_secret,
                                      coinbase_passphrase)

class Client():
    def place_market_buy(self, amount):
        return cb_auth_cli.place_market_order(product_id='BTC-USD',
                                                side='buy',
                                                funds=amount)

    def place_market_sale(self, amount):
        return cb_auth_cli.place_market_order(product_id='BTC-USD',
                                                side='sell',
                                                funds=amount)

    def get_order(self, order_id):
        return cb_auth_cli.get_order(order_id)

    def account(self):
        return cb_auth_cli.get_accounts()

    def ticker(self, currency):
        return cb_pub_cli.get_product_ticker(product_id=currency)


    def usd_balance(self):
        result = cb_auth_cli.get_account(cb_usd_acc_num).get('balance')
        if result != None:
            return float(result)
        else:
            return 0

    def btc_balance(self):
        result = cb_auth_cli.get_account(cb_btc_acc_num).get('balance')
        if result != None:
            return float(result)
        else:
            return 0

    def current_btc_price(self):
        return cb_pub_client.ticker('BTC-USD').get('price')

