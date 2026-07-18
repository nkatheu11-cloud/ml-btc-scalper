import MetaTrader5 as mt5



def trend_confirmation(symbol):


    rates = mt5.copy_rates_from_pos(

        symbol,

        mt5.TIMEFRAME_M15,

        0,

        50

    )


    if rates is None:
        return False



    close = rates[-1][4]


    average = sum(
        r[4] for r in rates
    ) / len(rates)



    if close > average:

        return 1


    elif close < average:

        return -1


    return 0
