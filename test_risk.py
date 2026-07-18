import MetaTrader5 as mt5

from mt5_connector import MT5Connector
from risk import RiskManager

bot = MT5Connector()

bot.connect()

risk = RiskManager()

print("Balance:", risk.account_balance())

print("Spread:", risk.current_spread())

print("Can Trade:", risk.can_trade())

price = mt5.symbol_info_tick("BTCUSD.m").ask

sl, tp = risk.stop_loss_take_profit(
    "BUY",
    price,
    atr=120
)

print("SL:", sl)

print("TP:", tp)

lot = risk.lot_size(price, sl)

print("Lot:", lot)

bot.shutdown()
