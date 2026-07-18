"""
strategy.py

Main trading decision engine.

Combines:
- Market data
- AI prediction
- Risk control
- Trade execution
"""

import logging
import MetaTrader5 as mt5

from config import SYMBOL

from predict import predict_signal
from execution import send_order
from safety import safety_check
from config import SYMBOL
from advanced_risk import account_equity_check
from exposure import exposure_allowed
from loss_control import trading_allowed

def check_existing_position():
    """
    Prevent opening multiple trades
    """

    positions = mt5.positions_get(
        symbol=SYMBOL
    )


    if positions:
        return True


    return False



def run_strategy():

    logging.info(
        "Running strategy..."
    )


    # Check if trade already exists

    if check_existing_position():

        logging.info(
            "Existing position detected. Skipping trade."
        )

        return



    # Get AI prediction
    if not safety_check(SYMBOL):

    logging.info(
        "Safety check failed. No trade."
    )

    return
    if not account_equity_check():

    logging.warning(
        "Equity protection active"
    )

    return



if not exposure_allowed():

    logging.warning(
        "Exposure limit reached"
    )

    return



if not trading_allowed():

    logging.warning(
        "Loss streak protection active"
    )

    return
    signal = predict_signal()


    logging.info(
        f"AI signal: {signal}"
    )



    # Execute trade

    if signal == 1:

        logging.info(
            "BUY signal detected"
        )

        send_order(1)



    elif signal == -1:

        logging.info(
            "SELL signal detected"
        )

        send_order(-1)



    else:

        logging.info(
            "No valid trade signal"
        )
