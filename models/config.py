"""
Configuration
"""

import MetaTrader5 as mt5

# ===========================
# Trading
# ===========================

SYMBOL = "BTCUSD.m"

TIMEFRAME = mt5.TIMEFRAME_M1

MAGIC = 987654

COMMENT = "ML_BTC_SCALPER"

# ===========================
# Risk Management
# ===========================

RISK_PER_TRADE = 0.01

RISK_REWARD = 2.0

ATR_SL_MULTIPLIER = 1.5

MAX_SPREAD = 20

MAX_OPEN_TRADES = 1

MAX_DAILY_LOSS = 0.05

# ===========================
# Indicators
# ===========================

FAST_EMA = 9

SLOW_EMA = 21

RSI_PERIOD = 14

ATR_PERIOD = 14

# ===========================
# Machine Learning
# ===========================

TRAIN_BARS = 50000

MODEL_FILE = "models/btc_model.pkl"

LOOKAHEAD = 5

BUY_THRESHOLD = 0.0015

SELL_THRESHOLD = -0.0015

# ===========================
# Runtime
# ===========================

LOG_LEVEL = "INFO"

CHECK_INTERVAL = 5

HISTORY_BARS = 500

# ==============================
# SAFETY SETTINGS
# ==============================

MAX_OPEN_TRADES = 1

MAX_DAILY_LOSS = 50     # account currency

MAX_SPREAD = 50         # points


# Trading hours (server time)

START_HOUR = 0

END_HOUR = 23



# Logging

TRADE_LOG_FILE = "trades.csv"
