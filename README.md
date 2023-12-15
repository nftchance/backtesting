# Backtesting

> [!TIP]
> If you are a burger, the API used for crypto prices will fail. You may choose to use a VPN based somewhere that crypto laws are chill.

This repository provides a base template to do backtesting on Equities and Cryptocurrencies.

```ml
Yahoo - 'Provider for equity prices.'
Binance - 'Provider for crypto prices.'
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Database

All data is stored in a local SQLite database. I recommend using a tool such as [TablePlus](https://tableplus.com/) anytime you would like to interact with the database outside of the Python environment.
