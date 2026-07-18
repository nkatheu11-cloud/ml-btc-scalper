"""
Feature importance analyzer
"""

import joblib



def show_importance(model,features):


    importance = zip(
        features,
        model.feature_importances_
    )


    ranking = sorted(
        importance,
        key=lambda x:x[1],
        reverse=True
    )


    for name,value in ranking:

        print(
            name,
            round(value,4)
        )
