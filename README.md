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
open,
high,
low,
close,
tick_volume,
ema_fast,
ema_slow,
rsi,
atr,
macd,
macd_signal,
macd_hist,
bb_upper,
bb_lower,
bb_width,
momentum,
returns,
body,
range,
upper_wick,
lower_wick,
ema_distance,
ema_fast_slope,
ema_slow_slope,
atr_ratio,
volume_ma.
volume_ratio.

**Run**

python test_feature_engineering.py

You should see something similar to

ema_fast
ema_slow
ema_distance
...

label

 0    610
 1    190
-1    180

**Run the training

Open your terminal inside the project folder and run:

Command
**
python train_model.py

**What will happen**

Connect to MT5.

Download 50,000 one-minute BTCUSD candles.

Calculate all indicators.

Create BUY / SELL / HOLD labels.

Train an XGBoost model.

Evaluate the model.

Save the model to models/btc_model.pkl.

**Expected output**

You should see something similar to:

Accuracy: 0.61

Classification Report:

precision recall f1-score support

0 0.58 0.55 0.56 2100

1 0.65 0.70 0.67 4300

2 0.59 0.54 0.56 2200

**Top 10 Features:**

feature

	

importance




ema_distance

	

0.143




macd_hist

	

0.112




rsi

	

0.098




atr_ratio

	

0.081




momentum

	

0.074

**Verify the model file was created

After training, check that this file exists:**

models/btc_model.pkl

This is the trained machine learning model that the live bot will use.

**Important**

Make sure train_model.py finishes successfully and creates models/btc_model.pkl.

Part 6 (predict.py) will load that file and use it to generate live BUY / SELL / HOLD predictions.

**Quick self-check**

confirm these:

Did python train_model.py run without crashing?

Did you see an Accuracy: value printed?

Did the file models/btc_model.pkl appear in the models folder?

Did the output show a list of Top 10 Features?

**Run**

python test_predict.py

**Example output**

{
 'signal': 'BUY',
 'confidence': 0.91,
 'probabilities': {
     'SELL': 0.04,
     'HOLD': 0.05,
     'BUY': 0.91
 }
}

**Improvement before live trading

I recommend adding a confidence filter so the bot doesn't trade on weak predictions:**

result = predictor.predict(df)

if result["confidence"] < 0.75:
    return None

signal = result["signal"]

if signal == "HOLD":
    return None

return signal

**Run**
python test_risk.py

example output
Balance: 1000.00

Spread: 15.0

Can Trade: True

SL: 63980.25

TP: 64460.25

Lot: 0.02

**Run**

powershell 
python test_execution.py

Expected result:

INFO: Order successful: xxxxxxxx

or if your account blocks trading:

Order failed: ...

**Important check**

Your predict.py must return:

1

for BUY

-1

for SELL

0

for HOLD

Example:

return prediction

where:

prediction = 1

**Run**

Expected:

INFO: Running strategy...
INFO: AI signal: 1
INFO: BUY signal detected
INFO: Order successful

or:

INFO: Existing position detected. Skipping trade.

**Update config.py**
Make sure you have:

LOOP_TIME = 60

This means:

Check market
Make decision
Wait 60 seconds
Repeat

For BTCUSD M1 trading this is suitable.
