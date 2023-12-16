import datetime
import pandas as pd
import yfinance as yf

from pandas_datareader import data as pdr

from pull.pull import Puller

yf.pdr_override()


class Equity(Puller):
    def __init__(self, database, symbols_csv='equity/symbols.csv'):
        self.database = database
        self.symbols_csv = symbols_csv

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
            data = pdr.get_data_yahoo(
                symbol,
                start=start,
                end=cursor,
                interval='1m'
            )

            if data.empty:
                cursor = end

            frames.append(data)
            cursor += datetime.timedelta(days=7)
            cursor = end if cursor > end else cursor
            start += datetime.timedelta(days=7)

        return pd.concat(frames)
