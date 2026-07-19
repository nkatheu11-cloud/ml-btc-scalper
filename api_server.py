from fastapi import FastAPI
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


    return result
