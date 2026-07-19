def ensemble_prediction(

        xgb_signal,

        lstm_probability,

        sentiment_score

):


    score = 0



    if xgb_signal == 1:

        score += 40


    elif xgb_signal == -1:

        score -= 40



    if lstm_probability > 0.6:

        score += 30


    elif lstm_probability < 0.4:

        score -= 30



    if sentiment_score > 0:

        score += 30


    else:

        score -= 30



    if score >= 50:

        return 1


    elif score <= -50:

        return -1


    return 0
