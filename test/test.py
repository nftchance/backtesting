import datetime
import pandas as pd

from backtesting import Backtest


class Test:
    def __init__(self, symbols, engine, strategy):
        self.symbols = symbols
        self.engine = engine
        self.strategy = strategy

    def resample(self, frame, interval):
        return frame.resample(interval).agg({
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last'
        })

    def backtest(self, interval='15min'):
        returns = []
        for symbol in self.symbols.name:
            query = f"""
            SELECT * FROM '{symbol}'
            WHERE Date < '{
                pd.to_datetime('today') - datetime.timedelta(days=30)
            }'
            """
            frame = pd.read_sql(query, self.engine).set_index('Date')
            frame.index = pd.to_datetime(frame.index)
            frame = self.resample(frame, interval)
            backtest = Backtest(
                frame,
                self.strategy,
                cash=100000,
                commission=.0015,
                exclusive_orders=True
            )
            output = backtest.run()
            backtest.plot()
            returns.append(output['Return [%]'])

        frame = pd.DataFrame(returns, index=self.symbols.name, columns=['ret'])
        n = 5 if len(self.symbols.name) > 5 else len(self.symbols.name)
        top_five = frame.nlargest(n, 'ret')

        return top_five, interval
