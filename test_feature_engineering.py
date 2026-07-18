import MetaTrader5 as mt5

from mt5_connector import MT5Connector

from indicators import Indicators

from feature_engineering import FeatureEngineering

bot = MT5Connector()

bot.connect()

df = bot.get_rates(
    mt5.TIMEFRAME_M1,
    1000
)

df = Indicators.calculate(df)

X, y = FeatureEngineering.prepare_dataset(df)

print(X.head())

print()

print(y.value_counts())

bot.shutdown()
