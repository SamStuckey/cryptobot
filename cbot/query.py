from cbot.client import CoinbaseClient

cb_client = CoinbaseClient()

def btc_price_in_usd(currency):
    return cb_client.ticker(currency)['price']
