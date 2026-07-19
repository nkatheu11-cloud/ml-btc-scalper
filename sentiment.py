def sentiment_score(news):


    positive_words=[

    "bullish",

    "breakout",

    "adoption"

    ]


    negative_words=[

    "crash",

    "hack",

    "ban"

    ]


    score=0


    for word in news:

        if word in positive_words:

            score+=1


        if word in negative_words:

            score-=1



    return score
