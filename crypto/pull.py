import pandas as pd
from sqlalchemy import create_engine
from binance import Client


class Crypto:
    def __init__(self):
        self.client = Client()
        self.engine = create_engine('sqlite:///1_minute.db')

    def symbols(self):
        symbols = []
        for index, row in pd.read_csv(
            'crypto/symbols.csv',
            header=None
        ).iterrows():
            symbols.append(row[0])

        return symbols

    def get_minute_data(self, symbol, start='30 days ago UTC'):
        frame = pd.DataFrame(
            self.client.get_historical_klines(
                symbol,
                Client.KLINE_INTERVAL_1MINUTE,
                start
            )
        )

        if len(frame) == 0:
            return None

        frame = frame[[0, 1, 2, 3, 4]]
        frame.columns = ['Date', 'Open', 'High', 'Low', 'Close']
        frame.Date = pd.to_datetime(frame.Date, unit='ms')
        frame.set_index('Date', inplace=True)
        frame = frame.astype(float)
        return frame

    def get_symbol(self, symbol):
        print('Getting {}...'.format(symbol))

        frame = self.get_minute_data(symbol)

        if frame is None:
            return None

        frame.to_sql(symbol, self.engine)

        return frame

    def get_symbols(self, symbols=pd.read_csv(
        'crypto/symbols.csv',
        header=None
    )):
        responses = []
        rows = symbols.iterrows()

        for index, row in rows:
            symbol = row[0]
            responses.append(self.get_symbol(symbol))

        return responses

    def get_symbols_in_db(self):
        return pd.read_sql(
            """SELECT name FROM sqlite_master WHERE type='table'""",
            self.engine
        )

    def get_symbol_in_db(self, symbol):
        return pd.read_sql(
            """SELECT * FROM '{}'""".format(symbol),
            self.engine
        )
