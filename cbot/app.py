from cbot.clients.cb_client  import CbClient
from cbot.models.order       import Order
from cbot.algorithms.bellows import Bellows
from cbot.bank               import Bank
from cbot.transactor         import Transactor
from cbot.logger             import Logger

class Cbot:
    margin                = 0.011
    purchase_percentage   = 0.05
    default_purchase_size = 50
    markets               = ['BTC-USD', 'ETH-USD']
    transactors           = []

    def __init__(self):
        self.client = CbClient()
        self.bank   = Bank(self.markets, self.client)
        self._create_transactors()

    def __call__(self, price, runs):
        self.runs = runs
        if price is None:
            return 0
        else:
            self.price = float(price)
            try:
                return self._run()
            except:
                e = sys.exc_info()[0]
                print('something went wrong')
                print(e)

    def _run(self):
        self._make_money()
        self._default_report()
        self._handle_run_count()

    def _create_transactors(self):
        algo = Bellows(self.margin)
        for coin in self.bank.coins:
            self.transactors.append(Transactor(coin,
                                                algo,
                                                self.purchase_percentage,
                                                self.default_purchase_size,
                                                self.client))

    def _default_report(self):
        if self.runs % 100 == 0:
            for transactor in self.transactors:
                Loger.default_report(transactor, self.usd_balance)
            Logger.report_cash_out_value(self.bank)

    def _handle_run_count(self):
        self.runs += 1
        if self.runs % 100 == 0:
            self.runs = 1

    def _make_money(self):
        self._run_transactions()

    def _run_transactions(self):
        for transactor in self.transactors:
            transactor.run()

    def _needs_update(self, ext_status, int_status):
        return ext_status != 'pending' and ext_status != int_status

