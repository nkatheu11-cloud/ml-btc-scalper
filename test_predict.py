import MetaTrader5 as mt5

from mt5_connector import MT5Connector
from predict import Predictor

bot = MT5Connector()

bot.connect()

df = bot.get_rates(
    mt5.TIMEFRAME_M1,
    500
)

predictor = Predictor()

result = predictor.predict(df)

print(result)

bot.shutdown()
