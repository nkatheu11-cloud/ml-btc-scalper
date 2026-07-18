import pandas as pd

from backtest import run_backtest, trades
from performance import generate_report



data=pd.read_csv(
    "BTCUSD_history.csv"
)



final_balance = run_backtest(
    data
)



print(
    f"Final Balance: {final_balance}"
)



generate_report(
    trades
)
