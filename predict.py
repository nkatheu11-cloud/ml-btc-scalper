"""
predict.py

Loads the trained model and generates
BUY / SELL / HOLD predictions.
"""

import joblib
import numpy as np

from config import MODEL_FILE
from feature_engineering import FeatureEngineering
from indicators import Indicators


class Predictor:

    def __init__(self):

        self.model = joblib.load(MODEL_FILE)

        self.features = FeatureEngineering.get_features()

    def predict(self, df):

        # Calculate indicators
        df = Indicators.calculate(df)

        # Use the latest candle
        last = df.iloc[-1:]

        # Keep only features used during training
        cols = [f for f in self.features if f in last.columns]

        X = last[cols]

        # Predict class
        prediction = self.model.predict(X)[0]

        # Class probabilities
       probability = model.predict_proba(
    features
)


confidence = max(
    probability[0]
)



if confidence < 0.60:

    return 0



prediction = model.predict(
    features
)


return prediction[0]

        # Convert XGBoost labels back
        # 0 -> SELL
        # 1 -> HOLD
        # 2 -> BUY

        if prediction == 2:
            signal = "BUY"

        elif prediction == 0:
            signal = "SELL"

        else:
            signal = "HOLD"

        return {

            "signal": signal,

            "confidence": confidence,

            "probabilities": {

                "SELL": float(probabilities[0]),

                "HOLD": float(probabilities[1]),

                "BUY": float(probabilities[2])

            }

        }
