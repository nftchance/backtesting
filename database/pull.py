import pandas as pd


class Database:
    def __init__(self, engine):
        self.engine = engine

    def get_symbols(self):
        return pd.read_sql(
            """SELECT name FROM sqlite_master WHERE type='table'""",
            self.engine
        )

    def get_symbol(self, symbol):
        return pd.read_sql(
            """SELECT * FROM '{}'""".format(symbol),
            self.engine
        )

    def has_symbol(self, symbol):
        return symbol in self.get_symbols().name.values
