#  [wipn] break out an analyzer and state object
class Bellows:
    trend = 'd' # assume on start so we don't buy right away
    def __init__(self, margin):
        #  [wipn] START HERE - i can't have current price heere... makes sense
        #  to break this out into two services?
        #  self.set_ceiling(current_price)
        #  self.set_floor(current_price)
        self.margin = margin

    def process_change(self, current_price):
        self._monitor_trend(current_price)

    def set_for_next(self, current_price):
        self._update_limits(current_price)

    def time_to_sell(self, current_price):
        return self._sales_rules_apply(current_price)

    def time_to_buy(self, current_price):
        return self._purchase_rules_apply(current_price) and self._funds_available()

    def _sales_rules_apply(self):
        return self._new_peak() or self._new_down_trend()

    def _monitor_trend(self, current_price):
        self._monitor_turns(current_price)
        self._monitor_extremes(current_price)

    def _update_limits(self, current_price):
        if current_price > self.ceiling or current_price < self.floor:
            self._set_ceiling(current_price)
            self._set_floor(current_price)
            self._reset_runs_in_price_box()

    def _new_peak(self):
        return self.trend == 'u' and (self.runs_at_peak == 101)

    def _new_valley(self):
        return self.trend == 'd' and (self.runs_in_valley == 101)

    def _moving_steadily_up(self, current_price):
        return self.trend == 'u' and self._above_ceiling(current_price)

    def _monitor_turns(self, current_price):
        if self._down_turn(current_price):
            print('down turn')
            self.trend = 'd'
            self.new_trend = True
            self._reset_extreme_counts()
        elif self._up_turn(current_price):
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

    def _up_turn(self, current_price):
        return self.trend == 'd' and self._above_ceiling(current_price)

    def _down_turn(self, current_price):
        return self.trend == 'u' and self._below_floor(current_price)

    def _purchase_rules_apply(self, current_price):
        return self._valley_or_uptick(current_price)  and not self._peaked()

    def _valley_or_uptick(self, current_price):
        return self._new_valley() or self._moving_steadily_up(current_price) or self._new_up_trend()

    def _peaked(self):
        return self._holding_at_peak() or self._new_peak()

    def _below_floor(self, current_price):
        return current_price <= self.floor

    def _above_ceiling(self, current_price):
        return current_price >= self.ceiling

    def _set_ceiling(self, current_price):
        self.ceiling = current_price * self.margin + current_price

    def _set_floor(self, current_price):
        self.floor = current_price - current_price * self.margin

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
