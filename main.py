"""
main.py

Main BTCUSD AI Trading Bot

Starts MT5 connection
Runs strategy continuously
"""

import time
import logging
import MetaTrader5 as mt5

from mt5_connector import connect_mt5
from strategy import run_strategy
from config import LOOP_TIME



# Logging setup

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s %(levelname)s: %(message)s"

)



def main():

    logging.info(
        "Starting BTCUSD AI Trading Bot"
    )


    # Connect to MT5

    if not connect_mt5():

        logging.error(
            "MT5 connection failed"
        )

        return



    logging.info(
        "MT5 connection successful"
    )



    # Main trading loop

    while True:

        try:

            run_strategy()


            logging.info(
                f"Waiting {LOOP_TIME} seconds..."
            )


            time.sleep(
                LOOP_TIME
            )



        except KeyboardInterrupt:

            logging.info(
                "Bot stopped manually"
            )

            break



        except Exception as e:

            logging.error(
                f"Bot error: {e}"
            )


            time.sleep(10)



    mt5.shutdown()


    logging.info(
        "MT5 shutdown complete"
    )



if __name__ == "__main__":

    main()
