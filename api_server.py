from fastapi import FastAPI
from bot_control import *
import MetaTrader5 as mt5


app=FastAPI(
    title="BTCUSD AI Command Center"
)



@app.get("/")
def home():

    return {
        "status":
        "BTCUSD AI BOT ONLINE"
    }



@app.get("/account")
def account():

    info=mt5.account_info()


    return {

        "balance":
        info.balance,


        "equity":
        info.equity,


        "profit":
        info.profit

    }



@app.get("/positions")
def positions():


    pos=mt5.positions_get()


    result=[]


    if pos:

        for p in pos:

            result.append({

                "symbol":
                p.symbol,

                "volume":
                p.volume,

                "profit":
                p.profit

            })
@app.post("/stop")
def stop():

    stop_bot()

    return {
        "message":
        "Bot stopped"
    }



@app.post("/start")
def start():

    start_bot()

    return {
        "message":
        "Bot started"

    return result
