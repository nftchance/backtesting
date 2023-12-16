import json

tickers = []

with open('equity/tickers.json') as f:
    data = json.load(f)

    for index in data:
        tickers.append(data[index]['ticker'])

with open('equity/symbols.csv', 'w') as f:
    for ticker in tickers:
        f.write("%s\n" % ticker)
