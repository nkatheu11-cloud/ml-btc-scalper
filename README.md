# ml-btc-scalper
ml trading bot

**step 1**

pip install -r requirements.txt

**step 2**

**you should see**

Connected to MetaTrader5

Trading Symbol: BTCUSD.m

AccountInfo(...)

SymbolInfo(...)

time open high low close tick_volume ...

MT5 Shutdown

**You get a symbol error**

If your broker uses another symbol, such as:

BTCUSD
BTCUSD.a
BTCUSD.pro
BTCUSD_i

then edit config.py:

SYMBOL = "YOUR_SYMBOL"

**Run:**

python test_indicators.py

**You should now see a DataFrame with columns similar to:**

time,
open
high
low
close
tick_volume
ema_fast
ema_slow
rsi
atr
macd
macd_signal
macd_hist
bb_upper
bb_lower
bb_width
momentum
returns
body
range
upper_wick
lower_wick
ema_distance
ema_fast_slope
ema_slow_slope
atr_ratio
volume_ma
volume_ratio
