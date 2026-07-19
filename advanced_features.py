import pandas as pd
import numpy as np



def generate_features(df):


    data=df.copy()


    # Momentum

    data["momentum"] = (

        data.close -

        data.close.shift(10)

    )



    # ATR


    high_low = (
        data.high -
        data.low
    )


    data["atr"] = (

        high_low

        .rolling(14)

        .mean()

    )



    # Price position


    data["range_position"] = (

        data.close -
        data.low

    ) / (

        data.high -
        data.low

    )



    # Candle body


    data["body"] = (

        abs(
            data.open -
            data.close
        )

    )



    return data.dropna()
