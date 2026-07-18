"""
backtest.py

Historical BTCUSD strategy tester
"""

import pandas as pd
import logging

from predict import predict_signal


INITIAL_BALANCE = 10000

balance = INITIAL_BALANCE

position = None

entry_price = 0


trades = []



def run_backtest(data):

    global balance
    global position
    global entry_price


    for index,row in data.iterrows():


        signal = predict_signal(row)


        price = row["close"]



        # OPEN BUY

        if signal == 1 and position is None:


            position = "BUY"

            entry_price = price


            logging.info(
                f"BUY @ {price}"
            )



        # OPEN SELL

        elif signal == -1 and position is None:


            position="SELL"

            entry_price=price


            logging.info(
                f"SELL @ {price}"
            )



        # CLOSE POSITION

        elif position:


            profit = 0


            if position=="BUY":

                profit = price-entry_price


            elif position=="SELL":

                profit = entry_price-price



            balance += profit


            trades.append({

                "type":position,

                "entry":entry_price,

                "exit":price,

                "profit":profit

            })


            position=None



    return balance
