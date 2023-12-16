import datetime
import pandas as pd
import yfinance as yf

from pandas_datareader import data as pdr
from sqlalchemy import create_engine

yf.pdr_override()


class Equity:
    def __init__(self, database):
        self.engine = create_engine(database)

    def symbols(self):
        symbols = []
        for index, row in pd.read_csv(
            'equity/symbols.csv',
            header=None
        ).iterrows():
            symbols.append(row[0])

        return symbols

    def get_minute_data(
        self,
        symbol,
        start=datetime.datetime.now() - datetime.timedelta(days=29),
        end=datetime.datetime.now()
    ):
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=29)
        cursor = start + datetime.timedelta(days=7)

        frames = []

        while cursor < end:
            frames.append(pdr.get_data_yahoo(
                symbol,
                start=start,
                end=cursor,
                interval='1m'
            ))
            cursor += datetime.timedelta(days=7)
            cursor = end if cursor > end else cursor
            start += datetime.timedelta(days=7)

        return pd.concat(frames)

    def get_symbol(self, symbol):
        print('Getting {}...'.format(symbol))

        frame = self.get_minute_data(symbol)

        if frame.empty:
            return None

        frame.to_sql(symbol, self.engine)

        return frame

    def get_symbols(self, symbols=pd.read_csv(
        'equity/symbols.csv',
        header=None
    )):
        responses = []
        rows = symbols.iterrows()

        for index, row in rows:
            symbol = row[0]
            responses.append(self.get_symbol(symbol))

        return responses
