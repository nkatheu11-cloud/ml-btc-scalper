# ml-btc-scalper
ml trading bot

step 1

pip install -r requirements.txt

step 2

you should see

Connected to MetaTrader5

Trading Symbol: BTCUSD.m

AccountInfo(...)

SymbolInfo(...)

time open high low close tick_volume ...

MT5 Shutdown

If you get a symbol error

If your broker uses another symbol, such as:

BTCUSD
BTCUSD.a
BTCUSD.pro
BTCUSD_i

then edit config.py:

SYMBOL = "YOUR_SYMBOL"
