import MetaTrader5 as mt5

from market_data import get_market_data



def collect_all_timeframes(symbol):


    data = {}


    data["M1"] = get_market_data(

        symbol,

        mt5.TIMEFRAME_M1

    )


    data["M5"] = get_market_data(

        symbol,

        mt5.TIMEFRAME_M5

    )


    data["M15"] = get_market_data(

        symbol,

        mt5.TIMEFRAME_M15

    )


    data["H1"] = get_market_data(

        symbol,

        mt5.TIMEFRAME_H1

    )


    return data
