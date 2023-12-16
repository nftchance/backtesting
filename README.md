# Backtesting

> [!TIP]
> If you are a burger, the API used for crypto prices will fail. You may choose to use a VPN based somewhere that crypto laws are chill.

This repository provides a base template to do backtesting on Equities and Cryptocurrencies that will get you up and running in seconds. You do not need to do any configuration or retrieval of API keys.

```ml
├─ Yahoo - "Provider for equity prices."
└─ Binance - "Provider for crypto prices."
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

All data is stored in a local SQLite database. I recommend using a tool such as [TablePlus](https://tableplus.com/) anytime you would like to interact with the database outside of the Python environment.

If your database has no data or is not up to date with all the symbols, run:

```bash
python pull.py
```

> [!NOTE]
> It will take several hours to sync the entire state of your database. It will be fine running a super long time and is setup to defend from unexpected errors. Just run the command and go do something else for the day.

With your database populated, you are now ready to run the tests that power the indicators and strategies. You can do so by returning to your terminal and running:

```bash
python test.py
```
