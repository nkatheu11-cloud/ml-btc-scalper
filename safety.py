"""
safety.py

Risk protection layer
"""

import MetaTrader5 as mt5
import datetime
import logging

from config import (
    MAX_OPEN_TRADES,
    MAX_SPREAD,
    START_HOUR,
    END_HOUR,
    MAX_DAILY_LOSS
)



def check_trade_count():

    positions = mt5.positions_get()


    if positions is None:
        return True


    if len(positions) >= MAX_OPEN_TRADES:

        logging.warning(
            "Maximum open trades reached"
        )

        return False


    return True



def check_spread(symbol):

    tick = mt5.symbol_info_tick(symbol)


    if tick is None:
        return False


    spread = (
        tick.ask - tick.bid
    )


    info = mt5.symbol_info(symbol)


    spread_points = spread / info.point


    if spread_points > MAX_SPREAD:

        logging.warning(
            f"Spread too high: {spread_points}"
        )

        return False


    return True



def check_trading_time():

    hour = datetime.datetime.now().hour


    if hour < START_HOUR or hour > END_HOUR:

        logging.info(
            "Outside trading hours"
        )

        return False


    return True



def safety_check(symbol):

    checks = [

        check_trade_count(),

        check_spread(symbol),

        check_trading_time()

    ]


    return all(checks)
