"""
train_model.py

Downloads historical BTCUSD M1 data,
creates features, trains an XGBoost model,
evaluates it, and saves the model.
"""

import os
import joblib
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

import MetaTrader5 as mt5

from config import TRAIN_BARS
from config import TIMEFRAME
from config import MODEL_FILE

from mt5_connector import MT5Connector
from indicators import Indicators
from feature_engineering import FeatureEngineering

from logger import logger


def train():

    logger.info("Starting model training")

    bot = MT5Connector()

    bot.connect()

    logger.info(f"Downloading {TRAIN_BARS} candles")

    df = bot.get_rates(
        TIMEFRAME,
        TRAIN_BARS
    )

    logger.info(f"Downloaded {len(df)} candles")

    df = Indicators.calculate(df)

    X, y = FeatureEngineering.prepare_dataset(df)

    X_train, X_test, y_train, y_test = (
        FeatureEngineering.split(X, y)
    )

    logger.info(f"Train samples: {len(X_train)}")

    logger.info(f"Test samples: {len(X_test)}")

    # XGBoost expects classes starting from 0
    # Convert: -1 -> 0, 0 -> 1, 1 -> 2

    y_train_xgb = y_train + 1
    y_test_xgb = y_test + 1

    model =XGBClassifier(

    n_estimators=500,

    max_depth=6,

    learning_rate=0.03,

    subsample=0.8,

    colsample_bytree=0.8,

    objective="multi:softmax",

    num_class=3

)

    logger.info("Training model...")

    model.fit(X_train, y_train_xgb)

    logger.info("Model training complete")

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test_xgb, predictions)

    print("Accuracy:", round(accuracy, 4))

    print("\nClassification Report:\n")

    print(classification_report(y_test_xgb, predictions))

    print("\nConfusion Matrix:\n")

    print(confusion_matrix(y_test_xgb, predictions))

    importance = pd.DataFrame({

        "feature": X.columns,

        "importance": model.feature_importances_

    }).sort_values("importance", ascending=False)

    print("\nTop 10 Features:\n")

    print(importance.head(10))

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, MODEL_FILE)

    logger.info(f"Model saved to {MODEL_FILE}")

    bot.shutdown()


if __name__ == "__main__":

    train()
FUTURE_BARS = 5
df["future_price"] = (
    df["close"]
    .shift(-FUTURE_BARS)
)


df["target"] = 0


df.loc[
df.future_price > df.close*1.001,
"target"
]=1


df.loc[
df.future_price < df.close*0.999,
"target"
]=-1
