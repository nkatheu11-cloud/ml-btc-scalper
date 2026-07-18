from telegram.ext import Application,CommandHandler



TOKEN="YOUR_TOKEN"



async def status(update,context):

    await update.message.reply_text(
        "BTCUSD AI Bot ONLINE"
    )



async def balance(update,context):

    import MetaTrader5 as mt5


    account = mt5.account_info()


    await update.message.reply_text(

        f"Balance: {account.balance}"

    )



app = Application.builder().token(
TOKEN
).build()



app.add_handler(

CommandHandler(
"status",
status
)

)


app.add_handler(

CommandHandler(
"balance",
balance
)

)


app.run_polling()
