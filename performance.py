"""
Performance statistics
"""


import pandas as pd



def generate_report(trades):


    df=pd.DataFrame(trades)


    total=len(df)


    wins=len(
        df[df.profit>0]
    )


    losses=len(
        df[df.profit<=0]
    )


    win_rate=0


    if total:

        win_rate=(
            wins/total
        )*100



    profit=df.profit.sum()



    print("===================")

    print(
        "BACKTEST REPORT"
    )

    print("===================")


    print(
        f"Trades: {total}"
    )


    print(
        f"Wins: {wins}"
    )


    print(
        f"Losses: {losses}"
    )


    print(
        f"Win Rate: {win_rate:.2f}%"
    )


    print(
        f"Profit: {profit:.2f}"
    )


    print("===================")
