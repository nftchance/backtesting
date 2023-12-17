import os

from multiprocessing import Pool
from sqlalchemy import create_engine

from crypto.pull import Crypto
from database.pull import Database
from equity.pull import Equity

os.environ["OPENBLAS_MAIN_FREE"] = "1"

database_url = 'sqlite:///1_minute.db'
engine = create_engine(database_url)
database = Database(engine)

crypto = Crypto(database)
equity = Equity(database)


def pull_crypto(symbol):
    crypto.get_symbol(symbol)


def pull_equity(symbol):
    equity.get_symbol(symbol)


if __name__ == '__main__':
    symbols = equity.get_symbols()
    with Pool() as p:
        p.map(pull_equity, symbols)

    symbols = crypto.get_symbols()
    with Pool() as p:
        p.map(pull_crypto, symbols)
