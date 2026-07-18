"""
Walk forward testing
"""

import pandas as pd



def split_data(df):


    size=len(df)


    train=df[:int(size*0.7)]


    test=df[int(size*0.7):]



    return train,test
