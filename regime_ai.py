def market_regime(
        volatility,
        trend
):


    if volatility > 0.03:

        return "HIGH_VOLATILITY"


    if trend > 0:

        return "BULL"


    if trend < 0:

        return "BEAR"


    return "RANGE"
