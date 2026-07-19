import pandas as pd



def performance():

    df=pd.read_csv(
        "professional_trades.csv"
    )


    return {

    "trades":
    len(df),


    "wins":
    len(
    df[df.profit>0]
    ),


    "losses":
    len(
    df[df.profit<0]
    )

    }
