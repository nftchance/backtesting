from multiprocessing import cpu_count, Pool
from crypto.pull import Crypto

crypto = Crypto()


def get_symbol(x):
    crypto.get_symbol(x)


if __name__ == '__main__':
    symbols = crypto.symbols()
    with Pool(cpu_count() - 1) as p:
        results = p.map(get_symbol, symbols)
        print(results)
