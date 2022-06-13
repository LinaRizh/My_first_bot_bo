
from telegram import Update
from telegram.ext import ApplicationBuilder, Updater, CommandHandler, CallbackContext
from commands import *


# async def hello(update: Update, context: CallbackContext) -> None:
#      await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def help(update: Update, context: CallbackContext):
#      await update.message.reply_text(f'/sum \n')

updater = ApplicationBuilder().token("5576391076:AAEJTKTMscmXNZDg6v8TveVWZ79yOWqscJo").build()

# def m_bot():
#     updater = Updater('5576391076:AAEJTKTMscmXNZDg6v8TveVWZ79yOWqscJo', use_context = True)

updater.add_handler(CommandHandler("help", help))
updater.add_handler(CommandHandler("sum", summ))
updater.add_handler(CommandHandler("mod", mod))
updater.add_handler(CommandHandler("div", div))
updater.add_handler(CommandHandler("mult", mult))
updater.add_handler(CommandHandler("sub", sub))
updater.add_handler(CommandHandler("sqrt", sqrt))
updater.add_handler(CommandHandler("pow", pow))

updater.run_polling()

