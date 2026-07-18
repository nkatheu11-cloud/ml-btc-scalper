"""
Advanced portfolio risk engine
"""


import MetaTrader5 as mt5
import logging

from config import (
    RISK_PER_TRADE,
    MAX_POSITION_VALUE,
    EQUITY_STOP_PERCENT
)



def account_equity_check():


    account = mt5.account_info()


    if account is None:

        return False



    balance = account.balance

    equity = account.equity



    loss_percent = (
        (balance-equity)
        /
        balance
    ) * 100



    if loss_percent >= EQUITY_STOP_PERCENT:


        logging.warning(
            "Equity protection triggered"
        )


        return False



    return True




def calculate_dynamic_lot(
        price,
        stop_loss
):


    account = mt5.account_info()


    if account is None:

        return 0.01



    balance = account.balance



    risk_money = (
        balance *
        RISK_PER_TRADE /
        100
    )



    stop_distance = abs(
        price-stop_loss
    )


    if stop_distance == 0:

        return 0.01



    lot = (
        risk_money /
        stop_distance
    )



    if lot < 0.01:

        lot=0.01



    return round(
        lot,
        2
    )
