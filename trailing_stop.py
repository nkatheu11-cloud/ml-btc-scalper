"""
Trailing stop manager
"""

import MetaTrader5 as mt5


TRAIL_DISTANCE = 100



def manage_trailing():

    positions = mt5.positions_get()


    if not positions:
        return



    for pos in positions:


        tick = mt5.symbol_info_tick(
            pos.symbol
        )


        if pos.type == mt5.POSITION_TYPE_BUY:


            new_sl = (
                tick.bid -
                TRAIL_DISTANCE *
                mt5.symbol_info(
                    pos.symbol
                ).point
            )


            if new_sl > pos.sl:


                modify_position(
                    pos,
                    new_sl
                )


        else:


            new_sl = (
                tick.ask +
                TRAIL_DISTANCE *
                mt5.symbol_info(
                    pos.symbol
                ).point
            )


            if pos.sl == 0 or new_sl < pos.sl:


                modify_position(
                    pos,
                    new_sl
                )



def modify_position(
        position,
        sl
):

    request = {

        "action":
        mt5.TRADE_ACTION_SLTP,

        "position":
        position.ticket,

        "sl":
        sl,

        "tp":
        position.tp

    }


    mt5.order_send(request)
