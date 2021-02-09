class Logger:
    @class_method
    def buy_report(self, algorithm):
        print('+++++++++++++++++ TIME TO BUY ++++++++++++++++++')
        print('    new valley: '          + str(self.algorithm.new_valley()))
        print('        trend: '           + self.algorithm.trend)
        print('        runs_in_valley: '  + str(self.algorithm.runs_in_valley))
        print('    moving_steadily_up: '  + str(self.algorithm.moving_steadily_up()))
        print('        above_ceiling: '   + str(self.algorithm.above_ceiling()))
        print('    new_up_trend: '        + str(self.algorithm.new_up_trend())) print('        new_trend: '       + str(self.algorithm.new_trend))

    @class_method
    def sell_report(self, algorithm):
        print('+++++++++++++++++ TIME TO SELL ++++++++++++++++++')
        print('    _new_peak: '        + str(self._new_peak()))
        print('        trend: '        + self.algorithm.trend)
        print('        runs_at_peak: ' + str(self.algorithm.runs_at_peak))
        print('    _new_down_trend: '  + str(self.algorithm.new_down_trend()))
        print('        new_trend: '    + str(self.new_trend))

    @class_method
    def default_report(self, transactor, balance):
        ceil_diff  = coin.price - algorithm.ceiling
        floor_diff = coin.price - algorithm.floor

        print('market: '           + self.market)
        print('Coin price: '       + str(coin.price))
        print('ceiling: '          + str(algorithm.ceiling))
        print('floor: '            + str(algorithm.floor))
        print('ceiling diff: '     + str(ceil_diff)
        print('floor diff: '       + str(floor_diff)
        print('**')
        print('Trend: '            + algorithm.trend)
        print('runs in price box:' + str(algorithm.runs_in_price_box))
        print('**')
        print('USD balance: '      + str(balance))
        print('Coin balance: '     + str(coin.balance))
        print('purchase size: '    + str(coin.purchase_size))
        print('---------------------------')

    @class_method
    def report_cash_out_value(self, bank):
        total = 0
        for coin in bank.coins():
            total += coin.worth
            print(str(coin.symbol) + ': ' + str(coin.worth))
        print('USD: ' + bank.usd_balance) 
        print '-----------------'
        print('total: ' + total + bank.usd_balance)
