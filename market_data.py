"""
Advanced market data collector
"""

import MetaTrader5 as mt5
import pandas as pd



def get_market_data(
        symbol,
        timeframe,
        bars=500
):


    rates = mt5.copy_rates_from_pos(

        symbol,

        timeframe,

        0,

        bars

    )


    if rates is None:

        return None



    df = pd.DataFrame(rates)


    df["time"] = pd.to_datetime(
        df["time"],
        unit="s"
    )


    return df
