import csv
import datetime



FILE="professional_trades.csv"



def save_trade(
        symbol,
        action,
        volume,
        price,
        confidence
):


    with open(
        FILE,
        "a",
        newline=""
    ) as f:


        writer=csv.writer(f)


        writer.writerow([

            datetime.datetime.now(),

            symbol,

            action,

            volume,

            price,

            confidence

        ])
