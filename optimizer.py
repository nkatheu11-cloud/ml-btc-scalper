"""
Parameter optimizer
"""


import itertools



ATR_VALUES=[
    1.5,
    2,
    2.5,
    3
]


TP_VALUES=[
    2,
    3,
    4,
    5
]



for atr,tp in itertools.product(
        ATR_VALUES,
        TP_VALUES):


    print(
    f"Testing ATR {atr} TP {tp}"
    )


    # run backtest here
