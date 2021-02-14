from cbot.logger       import Logger
from cbot.models.order import Order

class Transactor:
    runs_since_last_transaction = 0
    total_runs                  = 0

    def __init__(self, coin, algorithm, purchase_percentage, min_purchase):
        self.coin                = coin
        self.algorithm           = algorithm
        self.min_purchase        = min_purchase
        self.purchase_percentage = purchase_percentage

    def run(self, usd_balance):
        self.coin.update_price()
        self._run_available_transactions(usd_balance)
        self.total_runs += 1

    def purchase_size(self, usd_balance):
        percentage_based = usd_balance * self.purchase_percentage
        if percentage_based < self.min_purchase:
            return self.min_purchase
        else:
            return percentage_based

    def _run_available_transactions(self, usd_balance):
        if self.algorithm.time_to_buy(self.coin.price):
            self._run_buys(usd_balance)
        elif self.algorithm.time_to_sell(self.coin.price):
            self._run_sales()
        else:
            self.runs_since_last_transaction += 1
        self._update_pending_orders()

    #  [wipn] START HERE - create DB records from transactions
    def _run_buys(self, usd_balance):
        if self._purchase_funds_available(usd_balance):
            resp = self.coin.buy(self.purchase_size(usd_balance))
            if resp != None:
                Order.create(resp)
                self.last_transaction_rate = self.coin.price
                self.runs_since_last_transaction = 0
                Logger.buy_report(self.algorithm)

    def _run_sales(self):
        self._execute_sales()
        self.last_transaction_rate = self.coin.price
        self.runs_since_last_transaction = 0
        Logger.sell_report(self.algorithm)

    def _execute_sales(self):
        total_to_sell = 0.0
        for order in Order.profitable(self.coin.price, self.coin.market):
            total_to_sell += (order.filled_size or 0)
            order.sold = True
            order.save()

        if total_to_sell > 0:
            rounded_total = round(total_to_sell, 8)
            result = self.coin.sell(rounded_total)
            new_order = Order.create(result)

    def _purchase_funds_available(self, usd_balance):
        return usd_balance >= self.purchase_size(usd_balance)

    def _update_pending_orders(self):
        for order in Order.pending():
            cb_record = self.client.get_order(order.external_id)
            if self._needs_update(cb_record.get('status'), order.status):
                order.execute(cb_record)
