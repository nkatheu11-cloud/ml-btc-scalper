import MetaTrader5 as mt5

from mt5_connector import MT5Connector
from indicators import Indicators

bot = MT5Connector()

bot.connect()

df = bot.get_rates(
    mt5.TIMEFRAME_M1,
    200
)

df = Indicators.calculate(df)

print(df.tail())

print(df.columns)

bot.shutdown()
