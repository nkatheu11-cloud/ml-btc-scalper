"""
execution.py

Handles MT5 trade execution:
- Open BUY trades
- Open SELL trades
- Close trades
- Manage orders
"""

import MetaTrader5 as mt5
import logging

from config import SYMBOL
from risk import calculate_lot_size


def get_current_price(order_type):
    """
    Get current market price
    """

    tick = mt5.symbol_info_tick(SYMBOL)

    if tick is None:
        logging.error("Failed to get tick data")
        return None

    if order_type == mt5.ORDER_TYPE_BUY:
        return tick.ask

    return tick.bid



def send_order(signal):
    """
    Execute trading signal

    signal:
    1 = BUY
    0 = HOLD
    -1 = SELL
    """

    if signal == 0:
        logging.info("No trade signal")
        return None


    if signal == 1:
        order_type = mt5.ORDER_TYPE_BUY

    elif signal == -1:
        order_type = mt5.ORDER_TYPE_SELL

    else:
        logging.error("Invalid signal")
        return None


    price = get_current_price(order_type)

    if price is None:
        return None


    lot = calculate_lot_size()

   sl,tp = calculate_sl_tp(
    price,
    atr,
    order_type
) 
   from risk import calculate_sl_tp
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": lot,
        "type": order_type,
        "price": price,
        "deviation": 20,
        "magic": 100001,
        "comment": "BTCUSD AI Bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }


    result = mt5.order_send(request)


    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error(
            f"Order failed: {result.retcode}"
        )

    else:
        logging.info(
            f"Order successful: {result.order}"
        )


    return result



def close_position(ticket):
    """
    Close an open position
    """

    position = mt5.positions_get(ticket=ticket)


    if not position:
        logging.error("Position not found")
        return None


    position = position[0]


    if position.type == mt5.POSITION_TYPE_BUY:

        order_type = mt5.ORDER_TYPE_SELL
        price = mt5.symbol_info_tick(
            SYMBOL
        ).bid

    else:

        order_type = mt5.ORDER_TYPE_BUY
        price = mt5.symbol_info_tick(
            SYMBOL
        ).ask


    request = {

        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": position.volume,
        "type": order_type,
        "position": ticket,
        "price": price,
        "deviation": 20,
        "magic": 100001,
        "comment": "Close BTCUSD AI Bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,

    }


    result = mt5.order_send(request)


    if result.retcode == mt5.TRADE_RETCODE_DONE:
        logging.info(
            f"Position {ticket} closed"
        )

    else:
        logging.error(
            f"Close failed: {result.retcode}"
        )


    return result



def get_open_positions():

    positions = mt5.positions_get(
        symbol=SYMBOL
    )

    return positions
