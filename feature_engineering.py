"""
feature_engineering.py

Advanced BTCUSD AI features
"""

import pandas as pd
import numpy as np


def create_features(df):


    data = df.copy()



    # Returns

    data["returns"] = (
        data["close"]
        .pct_change()
    )



    # Moving averages

    data["ma_fast"] = (
        data["close"]
        .rolling(10)
        .mean()
    )


    data["ma_slow"] = (
        data["close"]
        .rolling(50)
        .mean()
    )



    # RSI

    delta = (
        data["close"]
        .diff()
    )


    gain = (
        delta
        .clip(lower=0)
        .rolling(14)
        .mean()
    )


    loss = (
        -delta
        .clip(upper=0)
        .rolling(14)
        .mean()
    )


    rs = gain / loss


    data["rsi"] = (
        100 -
        (100/(1+rs))
    )



    # Bollinger Bands

    middle = (
        data["close"]
        .rolling(20)
        .mean()
    )


    std = (
        data["close"]
        .rolling(20)
        .std()
    )


    data["bb_upper"] = (
        middle +
        2*std
    )


    data["bb_lower"] = (
        middle -
        2*std
    )



    # Volatility

    data["volatility"] = (
        data["returns"]
        .rolling(20)
        .std()
    )



    # Volume

    data["volume_change"] = (
        data["tick_volume"]
        .pct_change()
    )



    return data.dropna()
