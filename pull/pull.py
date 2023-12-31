import pandas as pd


class Puller:
    def __init__(self, puller, symbols_csv):
        self.symbols_csv = symbols_csv

    def get_symbol(self, symbol):
        symbol = str(symbol)

        if self.database.has_symbol(symbol):
            return self.database.get_symbol(symbol)

        frame = self.get_minute_data(symbol)

        if frame is None or frame.empty or symbol == 'nan':
            return None

        frame.to_sql(symbol, self.database.engine)

        return frame

    def get_symbols(self, symbols=None):
        if symbols is None:
            symbols = pd.read_csv(
                self.symbols_csv,
                header=None
            )

        responses = []
        rows = symbols.iterrows()

        for index, row in rows:
            symbol = row[0]
            responses.append(symbol)

        return responses

    def remove_symbol(self, symbol):
        symbols = pd.read_csv(
            self.symbols_csv,
            header=None
        )

        symbols = symbols[symbols[0] != symbol]

        symbols.to_csv(
            self.symbols_csv,
            header=None,
            index=False
        )

        return None
