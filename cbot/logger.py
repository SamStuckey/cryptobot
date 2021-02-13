class Logger:

    @classmethod
    def buy_report(self, algorithm):
        print('')
        print('+++++++++++++++++ TIME TO BUY ++++++++++++++++++')
        #  print('  new valley: '          + str(algorithm.new_valley()))
        #  print('      trend: '           + algorithm.trend)
        #  print('      runs_in_valley: '  + str(algorithm.runs_in_valley))
        #  print('  moving_steadily_up: '  + str(algorithm.moving_steadily_up()))
        #  print('      above_ceiling: '   + str(algorithm.above_ceiling()))
        #  print('  new_up_trend: '        + str(algorithm.new_up_trend()))
        #  print('      new_trend: '       + str(algorithm.new_trend))
        #  print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        #  print('')

    @classmethod
    def sell_report(self, algorithm):
        print('')
        print('+++++++++++++++++ TIME TO SELL ++++++++++++++++++')
        #  print('  _new_peak: '        + str(algorithm.new_peak()))
        #  print('      trend: '        + algorithm.trend)
        #  print('      runs_at_peak: ' + str(algorithm.runs_at_peak))
        #  print('  _new_down_trend: '  + str(algorithm.new_down_trend()))
        #  print('      new_trend: '    + str(new_trend))
        #  print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        #  print('')

    @classmethod
    def default_report(self, transactor, usd_balance):
        print('')
        print('+++++++++++++++++ DEFAULT REPORT ++++++++++++++++++')
        ceil_diff  = transactor.coin.price - transactor.algorithm.ceiling
        floor_diff = transactor.coin.price - transactor.algorithm.floor
        print('  market: '           + str(transactor.coin.market))
        print('  Coin price: '       + str(transactor.coin.price))
        print('  ceiling: '          + str(transactor.algorithm.ceiling))
        print('  floor: '            + str(transactor.algorithm.floor))
        print('  ceiling diff: '     + str(ceil_diff))
        print('  floor diff: '       + str(floor_diff))
        print('  **')
        print('  Trend: '            + transactor.algorithm.trend)
        print('  runs in price box:' + str(transactor.algorithm.runs_in_price_box))
        print('  **')
        print('  USD balance: '      + str(usd_balance))
        print('  Coin balance: '     + str(transactor.coin.balance))
        print('  purchase size: '    + str(transactor.purchase_size(usd_balance)))
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')

    @classmethod
    def report_cash_out_value(self, bank):
        print('$$$$$$$$$$$$$ COIN BALANCE VALUES: $$$$$$$$$$$$$')
        total = 0
        for coin in bank.coins:
            total += coin.worth()
            print('  ' + str(coin.symbol) + ': ' + str(coin.balance))
        print('  USD: ' + str(bank.usd_balance)) 
        print('  -----------------')
        print('  TOTAL: ' + str(bank.cash_out_value()))
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('')
