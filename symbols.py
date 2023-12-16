import os
import pandas as pd

from binance import Client
from ftplib import FTP

client = Client()
ftp = FTP('ftp.nasdaqtrader.com')

tickers = client.get_all_tickers()
symbols = [ticker['symbol'] for ticker in tickers]
symbols = pd.DataFrame(symbols)
symbols.to_csv(
    'crypto/symbols.csv',
    header=None,
    index=False
)

ftp.login()
ftp.cwd('symboldirectory')
ftp.retrbinary('RETR nasdaqlisted.txt', open('nasdaqlisted.txt', 'wb').write)
ftp.retrbinary('RETR otherlisted.txt', open('otherlisted.txt', 'wb').write)
ftp.quit()

symbols = []
with open('nasdaqlisted.txt', 'r') as f:
    lines = f.readlines()
    lines = lines[1:-1]
    lines = [line.split('|')[0] for line in lines]
    symbols.extend(lines)

with open('otherlisted.txt', 'r') as f:
    lines = f.readlines()
    lines = lines[1:-1]
    lines = [line.split('|')[0] for line in lines]
    symbols.extend(lines)

pd.DataFrame(symbols).to_csv('equity/symbols.csv', header=None, index=False)

os.remove('nasdaqlisted.txt')
os.remove('otherlisted.txt')
