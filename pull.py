from multiprocessing import cpu_count, Pool
from crypto.pull import Crypto
from equity.pull import Equity

database = 'sqlite:///1_minute.db'
crypto = Crypto(database)
equity = Equity(database)


def pull_crypto(x):
    crypto.get_symbol(x)


def pull_equity(x):
    equity.get_symbol(x)


if __name__ == '__main__':
    symbols = equity.symbols()
    with Pool(cpu_count() - 1) as p:
        p.map(pull_equity, symbols)

    symbols = crypto.symbols()
    with Pool(cpu_count() - 1) as p:
        p.map(pull_crypto, symbols)
