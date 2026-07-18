import csv
import datetime

from config import TRADE_LOG_FILE



def log_trade(
        action,
        price,
        volume
):

    with open(
        TRADE_LOG_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)


        writer.writerow([

            datetime.datetime.now(),

            action,

            price,

            volume

        ])
