"""
mt5_connector.py

Handles:
- MT5 connection
- Symbol selection
- Downloading historical data
- Account information
"""

from datetime import datetime
import time

import MetaTrader5 as mt5
import pandas as pd

from config import SYMBOL
from logger import logger


class MT5Connector:

    def __init__(self):
        self.connected = False

    def connect(self):
        """
        Connect to MetaTrader5
        """

        if mt5.initialize():

            logger.info("Connected to MetaTrader5")

            self.connected = True

        else:

            logger.error(mt5.last_error())

            raise Exception("Unable to initialize MT5")

        if not mt5.symbol_select(SYMBOL, True):

            raise Exception(f"Cannot select symbol {SYMBOL}")

        logger.info(f"Trading Symbol: {SYMBOL}")

    def shutdown(self):

        mt5.shutdown()

        self.connected = False

        logger.info("MT5 Shutdown")

    def account_info(self):

        info = mt5.account_info()

        if info is None:

            raise Exception("Cannot read account")

        return info

    def symbol_info(self):

        info = mt5.symbol_info(SYMBOL)

        if info is None:

            raise Exception("Cannot read symbol")

        return info

    def latest_tick(self):

        tick = mt5.symbol_info_tick(SYMBOL)

        if tick is None:

            raise Exception("Cannot read tick")

        return tick

    def get_rates(self, timeframe, bars):

        rates = mt5.copy_rates_from_pos(
            SYMBOL,
            timeframe,
            0,
            bars
        )

        if rates is None:

            raise Exception(mt5.last_error())

        df = pd.DataFrame(rates)

        df["time"] = pd.to_datetime(
            df["time"],
            unit="s"
        )

        return df

    def export_history(
        self,
        timeframe,
        bars,
        filename="data/history.csv"
    ):

        df = self.get_rates(
            timeframe,
            bars
        )

        df.to_csv(
            filename,
            index=False
        )

        logger.info(
            f"Saved {len(df)} candles to {filename}"
        )

        return df

    def wait_for_connection(self):

        while True:

            if mt5.initialize():

                logger.info("Connected")

                return

            logger.warning("Retrying MT5 connection...")

            time.sleep(5)
