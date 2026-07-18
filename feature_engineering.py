"""
feature_engineering.py

Creates ML features and labels from
historical market data.
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from config import (
    BUY_THRESHOLD,
    SELL_THRESHOLD,
    LOOKAHEAD
)


class FeatureEngineering:

    @staticmethod
    def create_labels(df):

        df = df.copy()

        # Future close price
        df["future_close"] = (
            df["close"]
            .shift(-LOOKAHEAD)
        )

        # Future return
        df["future_return"] = (
            (df["future_close"] - df["close"])
            / df["close"]
        )

        # BUY = 1
        # HOLD = 0
        # SELL = -1

        df["label"] = 0

        df.loc[
            df["future_return"] >= BUY_THRESHOLD,
            "label"
        ] = 1

        df.loc[
            df["future_return"] <= SELL_THRESHOLD,
            "label"
        ] = -1

        df.dropna(inplace=True)

        return df

    @staticmethod
    def get_features():

        return [

            "ema_fast",
            "ema_slow",

            "ema_distance",

            "ema_fast_slope",
            "ema_slow_slope",

            "rsi",

            "atr",

            "atr_ratio",

            "macd",

            "macd_signal",

            "macd_hist",

            "bb_width",

            "momentum",

            "returns",

            "body",

            "range",

            "upper_wick",

            "lower_wick",

            "tick_volume",

            "volume_ratio"

        ]

    @staticmethod
    def prepare_dataset(df):

        df = FeatureEngineering.create_labels(df)

        features = FeatureEngineering.get_features()

        # keep only features that exist
        features = [
            f
            for f in features
            if f in df.columns
        ]

        X = df[features]

        y = df["label"]

        return X, y

    @staticmethod
    def split(X, y):

        return train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42,

            shuffle=False

        )
