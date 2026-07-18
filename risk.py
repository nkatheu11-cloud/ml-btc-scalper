"""
risk.py

Professional risk management
"""

import MetaTrader5 as mt5

from config import SYMBOL


RISK_PERCENT = 1


ATR_MULTIPLIER_SL = 2

ATR_MULTIPLIER_TP = 4



def calculate_lot_size():

    account = mt5.account_info()

    if account is None:
        return 0.01


    balance = account.balance


    risk_amount = (
        balance *
        RISK_PERCENT /
        100
    )


    # BTCUSD conservative size

    lot = risk_amount / 1000


    if lot < 0.01:
        lot = 0.01


    return round(lot,2)



def calculate_sl_tp(
        price,
        atr,
        order_type
):

    if order_type == mt5.ORDER_TYPE_BUY:


        stop_loss = (
            price -
            atr * ATR_MULTIPLIER_SL
        )


        take_profit = (
            price +
            atr * ATR_MULTIPLIER_TP
        )


    else:


        stop_loss = (
            price +
            atr * ATR_MULTIPLIER_SL
        )


        take_profit = (
            price -
            atr * ATR_MULTIPLIER_TP
        )


    return stop_loss, take_profit
