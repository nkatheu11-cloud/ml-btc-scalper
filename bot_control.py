bot_running=True



def stop_bot():

    global bot_running

    bot_running=False



def start_bot():

    global bot_running

    bot_running=True



def status():

    return bot_running
