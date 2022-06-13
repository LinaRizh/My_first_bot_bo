from telegram import Update
from telegram.ext import CallbackContext
import math
from log import *

async def help(update: Update, context: CallbackContext):
    logger(update, context)
    await update.message.reply_text(f'/sum - сумма \n /sub -разность \n /mult - умножение \n /div - деление \n /mod - \
        остаток от деления \n /sqrt - корень квадратный \n /pow - возведение в степень ')
def str_to_num(znach):
    itog = []
    for i in znach: 
        if '.' in i and i.replace('.', '').isdigit():
            itog.append(float(i))
        elif 'j' in i:
            itog.append(complex(i))
        elif i.isdigit():
            itog.append(int(i))
    return itog

async def summ(update: Update, context: CallbackContext):
    logger(update, context)
    msg = update.message.text
    znach = msg.split()
    l = str_to_num(znach)
    answer = l[0] + l[1]
    await update.message.reply_text(f'{answer}')

async def sub(update: Update, context: CallbackContext):
    logger(update, context)
    msg = update.message.text
    znach = msg.split()
    l = str_to_num(znach)
    answer = l[0] - l[1]
    await update.message.reply_text(f'{answer}')

async def mult(update: Update, context: CallbackContext):
    logger(update, context)
    msg = update.message.text
    znach = msg.split()
    l = str_to_num(znach)
    answer = l[0] * l[1]
    await update.message.reply_text(f'{answer}')

async def div(update: Update, context: CallbackContext):
    logger(update, context)
    msg = update.message.text
    znach = msg.split()
    l = str_to_num(znach)
    answer = l[0] / l[1]
    await update.message.reply_text(f'{answer}')

async def sqrt(update: Update, context: CallbackContext):
    logger(update, context)
    msg = update.message.text
    znach = msg.split()
    if '.' in znach[1] and znach[1].replace('.', '').isdigit():
        answer = math.sqrt(float(znach[1]))
        await update.message.reply_text(f'{answer}')
    elif znach[1].isdigit():
        answer = math.sqrt(int(znach[1]))
        await update.message.reply_text(f'{answer}')
    else: await update.message.reply_text(f'Невозможно вычислить корень заданного числа')

async def mod(update: Update, context: CallbackContext):
    logger(update, context)
    msg = update.message.text
    znach = msg.split()
    l = str_to_num(znach)
    if type(l[0]) == complex or type(l[1]) == complex:
        await update.message.reply_text(f'Невозможно вычислить остаток от деления')
    else:
        answer = l[0] % l[1]
        await update.message.reply_text(f'{answer}')

async def pow(update: Update, context: CallbackContext):
    logger(update, context)
    msg = update.message.text
    znach = msg.split()
    l = str_to_num(znach)
    answer = l[0] ** l[1]
    await update.message.reply_text(f'{answer}')