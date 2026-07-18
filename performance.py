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

def max_drawdown(trades):

    balance=0

    peak=0

    drawdown=0


    for trade in trades:

        balance += trade["profit"]


        if balance > peak:

            peak=balance


        dd=peak-balance


        if dd > drawdown:

            drawdown=dd


    return drawdown

print(
f"Max Drawdown: {max_drawdown(trades)}"
)
