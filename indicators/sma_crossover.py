from backtesting.lib import crossover
from backtesting.test import SMA

from strategies.types.trailing_stop_loss import TrailingStrategy


class SmaCrossOver(TrailingStrategy):
    n1 = 10
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(self.sma1, self.sma2):
            stop_loss = price - price * 0.03
            take_profit = price + price * 0.04
            self.buy(sl=stop_loss, tp=take_profit)
        elif crossover(self.sma2, self.sma1):
            self.sell()
