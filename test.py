from crypto.pull import Crypto
from indicators.sma_crossover import SmaCrossOver
from test.test import Test

crypto = Crypto()
symbols = crypto.get_symbols_in_db()

if len(symbols) == 0:
    raise Exception("""No symbols in database. Do one of the below:
    1.) Run `python pull.py` to populate database.
    2.) Run `git pull` to get the latest public database.
    """)

test = Test(symbols, crypto.engine, SmaCrossOver)
test.backtest('15min')
