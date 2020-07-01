import cbpro
from Robinhood import Robinhood
from decouple import config

coinbase_key        = config('CB_API_PKEY')
coinbase_secret     = config('CB_API_SKEY')
coinbase_passphrase = config('CB_PASSPHRASE')
robinhood_qr        = config('RH_QR')
robinhood_username  = config('RH_UN')
robinhood_password  = config('RH_PW')

cb_pub_cli  = cbpro.PublicClient()
cb_auth_cli = cbpro.AuthenticatedClient(coinbase_key,
                                      coinbase_secret,
                                      coinbase_passphrase)

rh_client = Robinhood()
rh_client.login(username=robinhood_username,
              password=robinhood_password,
              qr_code=robinhood_qr)

class CoinbaseClient():
    def account(self):
        return cb_auth_cli.get_accounts()

    def ticker(self, currency):
        return cb_pub_cli.get_product_ticker(product_id=currency)

class RobinhoodClient():
    def __init__(self):
        rh_client
        return None

    def account(self):
        return rh_client.get_accounts()

    def instruments(self, symb):
        return rh_client.instruments("GEVO")[0]

    def buy(self):
        rh_client.place_market_order(instrument_URL='wipn',
                                    symbol='BTC',
                                    time_in_force=self.time_in_force,
                                    price=self._buy_price(),
                                    quantity=quantity)

    def build_order(self):
        data = {
            instrument: "URL should be defined already",
            symbol: "BTC-USD",
            account: "URL - account", # should be hardcoded, where do i get this?
            type: "market or limit",
            time_in_force: "gfd, gtc, ioc, or opg", # wipn what do these symbols stand for?
            trigger: "immediate or stop", # req - wipn what's the correlation between this and type
            type: "market or limit",
            price: "Float - what im willing to accept",
            stop_price: "Fload - only valid if trigger quals stop",
            quantity: "num shares to sell, eg. 0.01234 for BTC",
            side: "buy or sell",
            extended_hours: "Bool, can this be executed after hours?",
            override_day_trade_checks: "Bool - wipn this could be important?  but not worth fucking with if i dont need it",
            override_dtbp_checks: "Bool - not sure what this means"
        }
        return data
        #  {
        #      instrument: "URL should be defined already",
        #      symbol: "probably BTC-USD",
        #      account: "URL - account", # should be hardcoded, where do i get this?
        #      type: "market or limit",
        #      time_in_force: "gfd, gtc, ioc, or opg", # wipn what do these symbols stand for?
        #      trigger: "immediate or stop", # req - wipn what's the correlation between this and type
        #      type: "market or limit",
        #      price: "Float - what im willing to accept",
        #      stop_price: "Fload - only valid if trigger quals stop",
        #      quantity: "num shares to sell, eg. 0.01234 for BTC",
        #      side: "buy or sell",
        #      extended_hours: "Bool, can this be executed after hours?",
        #      override_day_trade_checks: "Bool - wipn this could be important?  but not worth fucking with if i dont need it",
        #      override_dtbp_checks: "Bool - not sure what this means"
        #  }

