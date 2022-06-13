from telegram import Update
from telegram.ext import CallbackContext

def logger (update: Update, context: CallbackContext):
    file = open('log.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}')
    file.close()