from cbot.client     import Client
from cbot.model      import Order
from cbot.db         import session

class Cbot:
    def __init__(self):
        self.client         = Client()
        self._set_purchase_size()
        self.runs           = 0
        print(self.purchase_size)
        result = self.client.place_market_sale(str(self.purchase_size))
        print(result)

    def __call__(self, price):
        pass
         #  if price is None:
         #      return
         #  else
         #      self.price = price
         #      self._run()

    def _run(self):
        if self.runs == 0:
            self._first_pass_setup()
        elif self.runs == 1:
            self._second_pass_setup()
        else:
            self._make_money()
        self.runs = self.runs + 1
        print(self.runs)
        if runs == 1000:
            self.adjust_purchase_size()
            self.runs = 3

    def adjust_purchase_size(self):
        if self._double_profit():
            self._set_purchase_size()

    def _double_profit(self):
        return self.client.usd_balance >= self.purchase_size * 200

    def _first_pass_setup(self):
        self.price                  = self.price
        self.last_trasnsaction_rate = self.price
        self._set_ceiling()
        self._set_floor()

    def _set_purchase_size(self):
        self.purchase_size = round(self._calculate_increment(), 2)

    def _second_pass_setup(self):
        if self.price > self.last_transaction_rate:
            self.trend = 'up'
        else: 
            self.trend = 'down'

    def _make_money(self):
        self._monitor_trend()
        self._run_transactions()
        self._update_pending_orders()

    def _run_transactions(self):
        if self._time_to_buy():
            self.client.place_market_buy(self.purchase_size)
            self._last_transaction_rate = self.price
        elif self._time_to_sell():
            self._execute_sales()
            self._last_transaction_rate = self.price
        else:
            pass

    def _monitor_trend(self):
        if self._new_down_trend():
            self.trend = 'down'
        elif self._new_up_trend():
            self.trend = 'up'

    def _new_down_trend(self):
        return self.trend == 'up' and self._below_floor()

    def _new_up_trend(self):
        return self.trend == 'down' and self._above_ceiling()

    def _time_to_sell(self):
        # reversal of upward tren
        return self.trend == 'up' and self._below_floor()

    def _time_to_buy(self):
        return self._purchase_rules_apply() and self._funds_available()

    def _purchase_rules_apply(self):
        return self._moving_steadily_up() or self._moving_steadily_down()

    def _funds_available(self):
        return self.client.usd_balance() >= self.purchase_size

    def _moving_steadily_up(self):
        return self.trend == 'up' and self._above_ceiling()

    def _moving_steadily_down(self):
         return self.trend == 'below' and self._below_floor()

    def _below_floor(self):
        return self.price <= self.floor

    def _above_ceilng(self):
        return self.price >= self.ceiling

    def _set_ceiling(self):
        self.ceiling = self.price * 0.02 + self.price

    def _set_floor(self):
        self.floor = self.price - self.price * 0.04

    def _execute_sales(self):
        total_to_sell = 0
        for order in self._profitable_orders():
            total_to_sell = total_to_sell + float(order['btc_quantity'])
            #  [wipn] implement this
            order.mark_sale_pending()

        if total_to_sell > 0:
            self.client.place_market_sale(total_to_sell)

    #  [wipn] will this work for pending sales as well?
    def _update_pending_orders(self):
        for order in Order.pending():
            cb_record = self.client.get_order(order.external_id)

            if self._needs_update(cb_record.get('status'), order.status):
                order.execute_purchase(cb_record)

    def _needs_update(self, ext_status, int_status):
        return ext_status != 'pending' and ext_status != int_status

    def _profitable_orders(self):
        return Order.profitable(self.current_price)

    def _calculate_increment(self):
        return self.client.usd_balance() * float(0.05)
