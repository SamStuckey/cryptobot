from cbot.clients.cb_client  import CbClient
from cbot.algorithms.bellows import Bellows
from cbot.bank               import Bank
from cbot.transactor         import Transactor
from cbot.logger             import Logger
from cbot.models.order       import Order

class Cbot:
    margin                = 0.011
    purchase_percentage   = 0.05
    min_purchase          = 50
    markets               = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'BCH-USD', 'OXT-USD', 'XLM-USD']
    transactors           = []

    def __init__(self):
        self.client = CbClient()
        self.bank   = Bank(self.markets, self.client)
        self._create_transactors()

    def __call__(self, price, runs):
        print('RUN: ' + str(runs))
        self.runs = runs
        if price is None:
            return 0
        else:
            try:
                return self._run(float(price))
            except:
                e = sys.exc_info()[0]
                print('something went wrong')
                print(e)

    def test_run(self):
        pass
        #  from cbot.coin import Coin
        #  for order in Order.pending():
        #      cb_record = self.client.get_order(order.external_id)
        #      if self._needs_update(cb_record.get('status'), order.status):
        #          order.execute(cb_record)
        #  resp = coin.buy(50)
        #  print(resp)
        #  Order.create(resp)

    def _run(self, current_price): 
        if self.runs % 2 == 0:
            self._run_transactions(current_price)
        else:
            self._update_pending_orders()
        #  self._default_report()
        self._handle_run_count()

    def _create_transactors(self):
        for coin in self.bank.coins:
            self.transactors.append(Transactor(coin,
                                                Bellows(self.margin),
                                                self.purchase_percentage,
                                                self.min_purchase))


    def _update_pending_orders(self):
        for order in Order.pending():
            cb_record = self.client.get_order(order.external_id)
            if self._needs_update(cb_record.get('status'), order.status):
                order.execute(cb_record)

    def _default_report(self):
        if self.runs % 10 == 0:
            for transactor in self.transactors:
                Logger.default_report(transactor, self.bank.usd_balance)
            Logger.report_cash_out_value(self.bank)

    def _handle_run_count(self):
        self.runs += 1
        if self.runs % 100 == 0:
            self.runs = 1

    def _run_transactions(self, current_price):
        for transactor in self.transactors:
            transactor.run(self.bank.usd_balance)

    def _needs_update(self, ext_status, int_status):
        return ext_status != 'pending' and ext_status != int_status
