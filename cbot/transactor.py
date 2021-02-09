class Transactor:
    def __init__(self, coin, algorithm, client):
        self.runs_since_last_transaction = 0
        self.client                      = client
        self.coin                        = coin
        self.algorithm                   = algorithm

    def run(self):
        current_price = self.coin.update_price()
        self.algorithm.process_change(current_price)
        if self.algorithm.time_to_buy(current_price):
            self._run_buys(current_price)
        elif self.algorithm.time_to_sell(current_price):
            self._run_sales(current_price)
        else:
            self.runs_since_last_transaction += 1
        self.algorithm.set_for_next(current_price)

    def _run_buys(self, current_price):
        self.client.place_order(self.purchase_size)
        self.last_transaction_rate = current_price
        self.runs_since_last_transaction = 0

    def _run_sales(self, current_price):
        self._execute_sales(current_price)
        self.last_transaction_rate = current_price
        self.runs_since_last_transaction = 0

    def _execute_sales(self, current_price):
        total_to_sell = 0.0
        for order in Order.profitable(current_price, self.market):
            total_to_sell += (order.filled_size or 0)
            order.sold = True
            order.save()

        if total_to_sell > 0:
            rounded_total = round(total_to_sell, 8)
            result = self.client.place_market_sale(rounded_total)
            new_order = Order.create(result)
