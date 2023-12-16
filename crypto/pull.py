import pandas as pd
from binance import Client

from pull.pull import Puller


class Crypto(Puller):
    def __init__(self, database, symbols_csv='crypto/symbols.csv'):
        self.client = Client()
        self.database = database
        self.symbols_csv = symbols_csv

    def get_minute_data(self, symbol, start='30 days ago UTC'):
        data = self.client.get_historical_klines(
            symbol,
            Client.KLINE_INTERVAL_1MINUTE,
            start
        )

        frame = pd.DataFrame(data)

        if len(frame) == 0 or frame.empty:
            self.remove_symbol(symbol)
            return None

        frame = frame[[0, 1, 2, 3, 4]]
        frame.columns = ['Date', 'Open', 'High', 'Low', 'Close']
        frame.Date = pd.to_datetime(frame.Date, unit='ms')
        frame.set_index('Date', inplace=True)
        frame = frame.astype(float)
        return frame
