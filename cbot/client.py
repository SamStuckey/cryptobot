import cbpro
from decouple import config

coinbase_key        = config('CB_API_PKEY')
coinbase_secret     = config('CB_API_SKEY')
coinbase_passphrase = config('CB_PASSPHRASE')

cb_pub_cli  = cbpro.PublicClient()
cb_auth_cli = cbpro.AuthenticatedClient(coinbase_key,
                                      coinbase_secret,
                                      coinbase_passphrase)

class Client():
    #  returns {
    #      'id': '33f739ab-7908-4639-b972-3d662c7153ae',
    #      'product_id': 'BTC-USD',
    #      'side': 'buy',
    #      'stp': 'dc',
    #      'funds': '9.95024875',
    #      'specified_funds': '10',
    #      'type': 'market',
    #      'post_only': False,
    #      'created_at': '2020-07-06T00:21:00.390029Z',
    #      'fill_fees': '0',
    #      'filled_size': '0',
    #      'executed_value': '0',
    #      'status': 'pending',
    #      'settled': False
    #  }
    def place_market_order(self, amount):
        return cb_auth_cli.place_market_order(product_id='BTC-USD',
                                                side='buy',
                                                funds=amount)

    #  returns {
    #      'id': '33f739ab-7908-4639-b972-3d662c7153ae',
    #      'product_id': 'BTC-USD',
    #      'profile_id': '060c2162-a79f-4708-b504-01fbf80b716b',
    #      'side': 'buy',
    #      'funds': '9.9502487500000000',
    #      'specified_funds': '10.0000000000000000',
    #      'type': 'market',
    #      'post_only': False,
    #      'created_at': '2020-07-06T00:21:00.390029Z',
    #      'done_at': '2020-07-06T00:21:00.394Z',
    #      'done_reason': 'filled',
    #      'fill_fees': '0.0497509230870000',
    #      'filled_size': '0.00109674',
    #      'executed_value': '9.9501846174000000',
    #      'status': 'done',
    #      'settled': True
    #  }
    def get_order(self, order_id):
        return cb_auth_cli.get_order(order_id)

    def account(self):
        return cb_auth_cli.get_accounts()

    def ticker(self, currency):
        return cb_pub_cli.get_product_ticker(product_id=currency)

    def sell(self, order):
        cb_auth_cli.sell(price='200.00', #USD
                            size='0.01', #BTC
                            order_type='limit',
                            product_id='BTC-USD')

