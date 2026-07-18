import shutil
import datetime



def backup_model():


    filename = (
        "backup_model_"
        +
        str(datetime.datetime.now())
        +
        ".pkl"
    )


    shutil.copy(

        "model.pkl",

        filename

    )
