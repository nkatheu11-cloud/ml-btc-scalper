"""
Bot health monitoring
"""

import time
import datetime
import logging


LAST_HEARTBEAT = None



def heartbeat():

    global LAST_HEARTBEAT


    LAST_HEARTBEAT = datetime.datetime.now()


    logging.info(
        f"Heartbeat: {LAST_HEARTBEAT}"
    )



def is_alive():

    if LAST_HEARTBEAT is None:

        return False


    difference = (
        datetime.datetime.now()
        -
        LAST_HEARTBEAT
    )


    if difference.seconds > 600:

        return False


    return True
