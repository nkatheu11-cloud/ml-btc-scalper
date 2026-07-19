def approve_model(
        profit_factor,
        drawdown
):


    if profit_factor > 1.5 and drawdown < 10:

        return True


    return False
