"""
Bot supervisor

Restarts bot after crashes
"""

import subprocess
import time
import logging

from bot_config import RESTART_DELAY



while True:


    try:

        logging.info(
            "Starting BTCUSD bot"
        )


        process = subprocess.run(
            [
            "python",
            "main.py"
            ]
        )


    except Exception as e:


        logging.error(e)



    logging.warning(
        "Bot stopped. Restarting..."
    )


    time.sleep(
        RESTART_DELAY
    )
