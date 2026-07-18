import MetaTrader5 as mt5

from mt5_connector import MT5Connector

bot = MT5Connector()

bot.connect()

print(bot.account_info())

print(bot.symbol_info())

df = bot.get_rates(
    mt5.TIMEFRAME_M1,
    10
)

print(df)

bot.shutdown()
