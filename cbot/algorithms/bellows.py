class Bellows:
    trend = 'd' # assume on start so we don't buy right away
    runs_at_peak      = 0
    runs_in_valley    = 0
    runs_in_price_box = 0
    last_price        = None

    def __init__(self, margin):
        self.margin = margin

    def time_to_sell(self, current_price):
        self._refresh_analysis(current_price)
        return self.analysis.sell_rules_apply()

    def time_to_buy(self, current_price):
        self._refresh_analysis(current_price)
        return self.analysis.buy_rules_apply()

    def _review_previous_analysis(self):
        if self.last_price != None:
            self._conditionally_update_limits()
        else:
            self._reset_price_box()

    def _refresh_analysis(self, current_price):
        if current_price != self.last_price:
            self.last_price = self.current_price
            self.current_price = current_price
            self._run_analysis()

    def _run_analysis(self):
        self._review_previous_analysis()
        self._monitor_trend()

    def _sales_rules_apply(self):
        return self._new_peak() or self._new_down_trend()

    def _monitor_trend(self):
        self._monitor_turns()
        self._monitor_extremes()

    def _conditionally_update_limits(self):
        if self._out_of_price_box():
            self._reset_price_box()

    def _out_of_price_bos(self):
        return self.current_price > self.ceiling or self.current_price < self.floor

    def _reset_price_box(self):
        self._set_ceiling()
        self._set_floor()
        self._reset_runs_in_price_box()

    def _new_peak(self):
        return self.trend == 'u' and (self.runs_at_peak == 101)

    def _new_valley(self):
        return self.trend == 'd' and (self.runs_in_valley == 101)

    def _moving_steadily_up(self):
        return self.trend == 'u' and self._above_ceiling()

    def _monitor_turns(self):
        if self._down_turn():
            print('down turn')
            self.trend = 'd'
            self.new_trend = True
            self._reset_extreme_counts()
        elif self._up_turn():
            print('up turn')
            self.trend = 'u'
            self.new_trend = True
            self._reset_extreme_counts()
        else:
            self.new_trend = False
            self.runs_in_price_box += 1

    def _monitor_extremes(self):
        if self._holding_in_valley():
            self.runs_in_valley += 1
        elif self._holding_at_peak():
            self.runs_at_peak += 1
        else:
            self._reset_extreme_counts()

    def _reset_extreme_counts(self):
        self.runs_at_peak = 0
        self.runs_in_valley = 0

    def _new_down_trend(self):
        return self.trend == 'd' and self.new_trend

    def _new_up_trend(self):
        return self.trend == 'u' and self.new_trend

    def _up_turn(self):
        return self.trend == 'd' and self._above_ceiling()

    def _down_turn(self):
        return self.trend == 'u' and self._below_floor()

    def _purchase_rules_apply(self):
        return self._valley_or_uptick()  and not self._peaked()

    def _valley_or_uptick(self):
        return self._new_valley() or self._moving_steadily_up() or self._new_up_trend()

    def _peaked(self):
        return self._holding_at_peak() or self._new_peak()

    def _below_floor(self):
        return self.current_price <= self.floor

    def _above_ceiling(self):
        return self.current_price >= self.ceiling

    def _set_ceiling(self):
        self.ceiling = self.current_price * self.margin + self.current_price

    def _set_floor(self):
        self.floor = self.current_price - self.current_price * self.margin

    def _holding_at_peak(self):
        return self._holding() and self.trend == 'u'

    def _holding_in_valley(self):
        return self._holding() and self.trend == 'd'

    def _holding(self):
        return self.runs_in_price_box >= 1000

    def _reset_runs_in_price_box(self):
        self.runs_in_price_box = 0

    def _reset_extreme_counts(self):
        self.runs_in_valley = 0
        self.runs_at_peak   = 0
