"""
indicators.py

Calculates technical indicators used for
machine learning and live trading.
"""

import pandas as pd
import numpy as np

from config import (
    FAST_EMA,
    SLOW_EMA,
    RSI_PERIOD,
    ATR_PERIOD
)


class Indicators:

    @staticmethod
    def calculate(df):

        df = df.copy()

        # ==========================
        # EMA
        # ==========================

        df["ema_fast"] = (
            df["close"]
            .ewm(span=FAST_EMA, adjust=False)
            .mean()
        )

        df["ema_slow"] = (
            df["close"]
            .ewm(span=SLOW_EMA, adjust=False)
            .mean()
        )

        # ==========================
        # RSI
        # ==========================

        delta = df["close"].diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(RSI_PERIOD).mean()

        avg_loss = loss.rolling(RSI_PERIOD).mean()

        rs = avg_gain / (avg_loss + 1e-10)

        df["rsi"] = 100 - (100 / (1 + rs))

        # ==========================
        # ATR
        # ==========================

        prev_close = df["close"].shift(1)

        tr1 = df["high"] - df["low"]

        tr2 = (df["high"] - prev_close).abs()

        tr3 = (df["low"] - prev_close).abs()

        tr = pd.concat(
            [tr1, tr2, tr3],
            axis=1
        ).max(axis=1)

        df["atr"] = tr.rolling(
            ATR_PERIOD
        ).mean()

        # ==========================
        # MACD
        # ==========================

        ema12 = df["close"].ewm(
            span=12,
            adjust=False
        ).mean()

        ema26 = df["close"].ewm(
            span=26,
            adjust=False
        ).mean()

        df["macd"] = ema12 - ema26

        df["macd_signal"] = (
            df["macd"]
            .ewm(span=9, adjust=False)
            .mean()
        )

        df["macd_hist"] = (
            df["macd"]
            - df["macd_signal"]
        )

        # ==========================
        # Bollinger Bands
        # ==========================

        ma20 = df["close"].rolling(20).mean()

        std20 = df["close"].rolling(20).std()

        df["bb_upper"] = ma20 + 2 * std20

        df["bb_lower"] = ma20 - 2 * std20

        df["bb_width"] = (
            df["bb_upper"]
            - df["bb_lower"]
        )

        # ==========================
        # Momentum
        # ==========================

        df["momentum"] = (
            df["close"]
            - df["close"].shift(5)
        )

        # ==========================
        # Returns
        # ==========================

        df["returns"] = (
            df["close"]
            .pct_change()
        )

        # ==========================
        # Candle Features
        # ==========================

        df["body"] = (
            df["close"]
            - df["open"]
        )

        df["range"] = (
            df["high"]
            - df["low"]
        )

        df["upper_wick"] = (
            df["high"]
            - df[["open", "close"]].max(axis=1)
        )

        df["lower_wick"] = (
            df[["open", "close"]].min(axis=1)
            - df["low"]
        )

        # ==========================
        # EMA Distance
        # ==========================

        df["ema_distance"] = (
            df["ema_fast"]
            - df["ema_slow"]
        )

        # ==========================
        # EMA Slope
        # ==========================

        df["ema_fast_slope"] = (
            df["ema_fast"].diff()
        )

        df["ema_slow_slope"] = (
            df["ema_slow"].diff()
        )

        # ==========================
        # ATR Ratio
        # ==========================

        df["atr_ratio"] = (
            df["atr"]
            / df["atr"].rolling(20).mean()
        )

        # ==========================
        # Volume Features
        # ==========================

        if "tick_volume" in df.columns:

            df["volume_ma"] = (
                df["tick_volume"]
                .rolling(20)
                .mean()
            )

            df["volume_ratio"] = (
                df["tick_volume"]
                / df["volume_ma"]
            )

        # ==========================
        # Remove NaN rows
        # ==========================

        df.dropna(inplace=True)

        return df
