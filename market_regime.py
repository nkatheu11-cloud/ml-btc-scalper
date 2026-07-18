import pandas as pd



def detect_market(df):


    volatility = (
        df.close
        .pct_change()
        .std()
    )



    if volatility > 0.02:

        return "HIGH_VOLATILITY"



    return "NORMAL"
