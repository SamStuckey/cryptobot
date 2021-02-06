class Bellows:
    trend = 'd' # assume on start so we don't buy right away
    runs_since_last_transaction = 0

    # [wipn] START HERE - this relies on current price, figure out the best way
    # to pass it in on each subsequent run
    def __init__(self, margin):

    def monitor_trend(self):
        self._check_for_turns()
        self._check_for_extremes()

    def update_limits(self):
        if self.price > self.ceiling or self.price < self.floor:
            self._set_ceiling()
            self._set_floor()
            self._reset_runs_in_price_box()

    def _new_peak(self):
        return self.trend == 'u' and (self.runs_at_peak == 101)

    def new_valley(self):
        return self.trend == 'd' and (self.runs_in_valley == 101)

    def moving_steadily_up(self):
        return self.trend == 'u' and self._above_ceiling()

    def _check_for_turns(self):
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

    def _monitor_trend(self):
        self._check_for_turns()
        self._check_for_extremes()

    def _check_for_extremes(self):
        if self._holding_in_valley():
            self.runs_in_valley += 1
        elif self._holding_at_peak():
            self.runs_at_peak += 1
        else:
            self._reset_extreme_counts()

    def _reset_extreme_counts(self):
        self.runs_at_peak = 0
        self.runs_in_valley = 0

    def new_down_trend(self):
        return self.trend == 'd' and self.new_trend

    def new_up_trend(self):
        return self.trend == 'u' and self.new_trend

    def _up_turn(self):
        return self.trend == 'd' and self._above_ceiling()

    def _down_turn(self):
        return self.trend == 'u' and self._below_floor()

    def time_to_sell(self):
        return self._new_peak() or self._new_down_trend()

    def time_to_buy(self):
        return self._purchase_rules_apply() and self._funds_available()

    def _purchase_rules_apply(self):
        return self._valley_or_uptick()  and not self._peaked()

    def _valley_or_uptick(self):
        return self.new_valley() or self.moving_steadily_up() or self._new_up_trend()

    def _peaked(self):
        return self._holding_at_peak() or self._new_peak()

    def _below_floor(self):
        return self.price <= self.floor

    def _above_ceiling(self):
        return self.price >= self.ceiling

    def _set_ceiling(self):
        self.ceiling = self.price * self.margin + self.price

    def _set_floor(self):
        self.floor = self.price - self.price * self.margin

    def _holding_at_peak(self):
        return self._holding() and self.trend == 'u'

    def _holding_in_valley(self):
        return self._holding() and self.trend == 'd'

    def _stablabized(self):
        if self._holding_at_peak():
            return 'peak'
        elif self._holding_in_valley():
            return 'valley'
        else:
            return 'False'

    def _holding(self):
        return self.runs_in_price_box >= 1000

    def _reset_runs_since_last_transaction(self):
        self.runs_since_last_transaction = 0

    def _reset_runs_in_price_box(self):
        self.runs_in_price_box = 0
