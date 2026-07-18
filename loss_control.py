"""
Loss streak protection
"""


losses = 0



def record_trade(result):

    global losses


    if result < 0:

        losses += 1


    else:

        losses = 0



def trading_allowed():

    from config import MAX_LOSS_STREAK


    if losses >= MAX_LOSS_STREAK:

        return False


    return True
