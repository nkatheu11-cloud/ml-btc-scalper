"""
Automatic model retraining
"""

import subprocess
import datetime



def retrain():


    print(
    "Retraining model..."
    )


    subprocess.run(
        [
        "python",
        "train_model.py"
        ]
    )


    print(
    datetime.datetime.now(),
    "Model updated"
    )
