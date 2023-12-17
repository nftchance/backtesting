import numpy as np

from backtest import Strategy


class TrailingStrategy(Strategy):
    dollar_amount = 20.

    def init(self):
        super().init()

    def set_trailing_sl(self, dollar_amount: float = 6):
        self.dollar_amount = dollar_amount

    def next(self):
        super().next()
        index = len(self.data) - 1
        for trade in self.trades:
            if trade.is_long:
                trade.sl = max(
                    trade.sl or -np.inf,
                    self.data.Close[index] - self._dollar_amount
                )
            else:
                trade.sl = min(
                    trade.sl or np.inf,
                    self.data.Close[index] + self._dollar_amount
                )
