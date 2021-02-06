class Coin:
    min_price = 35

    def __init__(self, market, client):
        self.market   = market
        self.balance  = self.client.coin_balance(self.market)
        self.price    = self.client.coin_price(self.market)
        self._reset_runs_in_price_box()
        self._set_ceiling()
        self._set_floor()

    def update_trend(self):
        self.algorithm.monitor_trend()

    def _place_order(self, amount):
        result = self.client.place_market_buy(amount)
        print('####### buy API result #########')
        print(result)
        return Order.create(result)

    def _funds_available(self):
        return self.usd_balance >= self.purchase_size

    def _adjust_purchase_size(self):
        self._set_purchase_size()
        print('purchase size set to: ' + str(self.purchase_size))

    def worth(self):
        return self.balance * self.price

    def _set_purchase_size(self):
        self.purchase_size = round(self._calculate_purchase_size(), 2)

