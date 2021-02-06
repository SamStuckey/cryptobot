class Transactor:
    def __init__(self, coin, algorithm, client):
        self.algorithm = algorithm(coin.market)
        self.coin      = coin
        self.client    = client
        self._reset_runs_since_last_transaction()

    def run(self):
        if self.algorithm.time_to_buy():
            self._buy_report()
            self._run_buys()
        elif self.algorithm.time_to_sell():
            self._sell_report()
            self._run_sales()
        else:
            self.runs_since_last_transaction += 1

    def _reset_runs_since_last_transaction(self):
        self.runs_since_last_transaction = 0

    def _reset_extreme_counts(self):
        self.runs_in_valley = 0
        self.runs_at_peak   = 0

    def _run_buys(self):
        self.client.place_order(self.purchase_size)
        self.algorithm.last_transaction_rate = self.price
        self.algorithm._reset_runs_since_last()

    def _run_sales(self):
        self.algorithm.execute_sales()
        self.last_transaction_rate = self.price
        self.runs_since_last_transaction = 0

    def _execute_sales(self):
        total_to_sell = 0.0
        for order in Order.profitable(self.price, self.market):
            total_to_sell += (order.filled_size or 0)

        if total_to_sell > 0:
            rounded_total = round(total_to_sell, 8)
            result = self.client.place_market_sale(rounded_total)
            new_order = Order.create(result)
