"""
Exposure management
"""


import MetaTrader5 as mt5

from config import MAX_POSITION_VALUE



def current_exposure():


    positions = mt5.positions_get()


    exposure = 0



    if positions:


        for p in positions:

            tick = mt5.symbol_info_tick(
                p.symbol
            )


            exposure += (
                p.volume *
                tick.bid
            )


    return exposure




def exposure_allowed():


    if current_exposure() >= MAX_POSITION_VALUE:

        return False


    return True
