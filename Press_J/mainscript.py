#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import telebot
from datetime import datetime
import createxl
import schedule
import threading
import time
import logging
import hokky

# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)


start_time = datetime.now()
print("Start time is", start_time)
current_month = datetime.now().month

ids = [-679121440, 637382945, 769896242, 198279301, 1506914847, 1937774967, 5008614912, 875595915, 813043165,
       1302941769, 438913614, 589849594, 570554640, 434829667, 352963798, 1902176432, 225414375, 1012480666, 1509835469,
       375565529]

work_chanel =-679121440 # -645886619 
obj_keys = ["ОП", "Социология", "Матан", "УОП", "Физра", "Философия", "Англ", "Дискретка", "Физика"]
Token = '1967246442:AAEuMFRGo4Hoy0nhDKF5elXLv0j9MaGB4_E'
bot = telebot.TeleBot(Token)


def markup_gen():
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(obj_keys[0], callback_data=obj_keys[0])
    btn2 = telebot.types.InlineKeyboardButton(obj_keys[1], callback_data=obj_keys[1])
    btn3 = telebot.types.InlineKeyboardButton(obj_keys[2], callback_data=obj_keys[2])
    btn4 = telebot.types.InlineKeyboardButton(obj_keys[3], callback_data=obj_keys[3])
    btn5 = telebot.types.InlineKeyboardButton(obj_keys[4], callback_data=obj_keys[4])
    btn6 = telebot.types.InlineKeyboardButton(obj_keys[5], callback_data=obj_keys[5])
    btn7 = telebot.types.InlineKeyboardButton(obj_keys[6], callback_data=obj_keys[6])
    btn8 = telebot.types.InlineKeyboardButton(obj_keys[7], callback_data=obj_keys[7])
    btn9 = telebot.types.InlineKeyboardButton(obj_keys[8], callback_data=obj_keys[8])

    keyboard.row(btn1, btn2, btn3)
    keyboard.row(btn4, btn5, btn6)
    keyboard.row(btn7, btn8, btn9)

    return keyboard


def notify():
    hokky_str = hokky.gen()
    bot.send_message(work_chanel, hokky_str, reply_markup=markup_gen())


schedule.every().monday.at("16:00").do(notify)
schedule.every().tuesday.at("16:00").do(notify)
schedule.every().wednesday.at("17:49").do(notify)
schedule.every().thursday.at("16:00").do(notify)
schedule.every().friday.at("16:00").do(notify)
schedule.every().saturday.at("16:00").do(notify)

def go():
    while 1:
        schedule.run_pending()
        time.sleep(1)

t = threading.Thread(target=go, name="тест")
t.start()


@bot.callback_query_handler(func=lambda c: c.data in obj_keys)
def btn_pushed(callback_query: telebot.types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    createxl.create_xl()
    createxl.mark_xl(callback_query.from_user.username, callback_query.data)
    bot.send_message(callback_query.from_user.id, 'Сохранено, '+str(callback_query.from_user.username))


@bot.message_handler(commands=['start'])
def First(message):
    bot.send_message(message.chat.id,rf"Команды, для отметки: {obj_keys}")


@bot.message_handler(commands=['nt'])
def Notify(message):
    hokky_str = hokky.gen()
    bot.send_message(work_chanel, hokky_str, reply_markup=markup_gen())

@bot.message_handler(commands=obj_keys)
def Marking(message):
    bot.send_message(message.chat.id,"Одну секунду...")
    createxl.create_xl()
    fb_data=createxl.mark_xl(message.from_user.username,str(message.text[1 :len(message.text)]))
    print(fb_data, "Фидбек")
    bot.send_message(message.chat.id, str("Сохранено. ")+ str( fb_data[2])+" "+ str(fb_data[3]))


@bot.message_handler(commands=['таблица'])
def excell(message):
    #bot.send_document(message.chat.id, open(rf"//home//pi//Desktop//Press_J//months//{createxl.now_month()}.xlsx", "rb"))
    bot.send_document(message.chat.id, open(rf"//home//pi//Desktop//Press_J//months//{createxl.now_month()}.xlsx", "rb"))

@bot.message_handler(commands=['start_time'])
def start_time(message):
    bot.send_message(message.chat.id, start_time)
    print(message.chat.id)


print("Bot is polling")
bot.send_message(1931633887,"Bot is polling")

if __name__ == '__main__':
    while 1:
        try:
            bot.polling(True)
        except Exception:
            continue
        



