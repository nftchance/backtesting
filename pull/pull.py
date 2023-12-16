import pandas as pd


class Puller:
    def __init__(self, puller, symbols_csv):
        self.symbols_csv = symbols_csv

    def get_symbol(self, symbol):
        print('Getting {}...'.format(symbol))

        has_symbol = self.database.has_symbol(symbol)

        if has_symbol:
            return self.database.get_symbol(symbol)

        try:
            frame = self.get_minute_data(symbol)
        except Exception:
            frame = None

        if frame.empty or frame is None:
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
