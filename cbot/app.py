from cbot.client            import CbClient
from cbot.order             import Order
from cbot.algorithm.bellows import Bellows

class Cbot:
    margin = 0.011
    purchase_percentage = 0.05
    markets = ['BTC-USD', 'ETH-USD']

    def __init__(self):
        self.cb_client = CbClient()
        self.bank      = Bank(markets, cb_client)
        self._update_balances()
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
        algo = Bellows(coin, margin)
        self.transactors = []
        for coin in bank.coins:
            self.transactors.append(Transactor(coin, coin, cb_client, margin))

    def _default_report(self):
        if self.runs % 10 == 0:

            for transactor in self.transactors:
                transactor.report()
            self._report_cash_out_value()

    def _handle_run_count(self):
        self.runs += 1
        if self.runs % 100 == 0:
            self._adjust_purchase_size()
            self.runs = 2

    def _make_money(self):
        self._update_balances()
        self._run_transactions()
        self._update_pending_orders()
        self._update_limits()

    def _update_balances(self):
        self.usd_balance = self.cb_client.usd_balance()
        for coin in self.bank.coins:
            coin.update_balance()
            coin.track_trend()

    def _run_transactions(self):
        for transactor in self.transactors:
            transactor.run()

    def _update_limits(self):
        for coin in self.bank.coins:
            coin.update_limits()
    
    def _update_pending_orders(self):
        for order in Order.pending():
            cb_record = self.cb_client.get_order(order.external_id)
            if self._needs_update(cb_record.get('status'), order.status):
                order.execute(cb_record)

    def _needs_update(self, ext_status, int_status):
        return ext_status != 'pending' and ext_status != int_status

    def _calculate_purchase_size(self):
        percentage_based = self.usd_balance * self.purchase_percentage
        if percentage_based < self.min_price:
            return self.min_price
        else:
            return percentage_based
