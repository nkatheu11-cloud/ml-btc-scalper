import MetaTrader5 as mt5

from mt5_connector import connect_mt5
from execution import send_order


connect_mt5()

send_order(1)

mt5.shutdown()
