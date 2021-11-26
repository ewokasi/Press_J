#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import telebot
import subprocess
from datetime import datetime
import createxl

start_time = datetime.now()
print("Start time is", start_time)
current_month = datetime.now().month

obj_keys = ["линал", "матанал", "история", "культура", "англ", "физра", "бжд", "инфа"]

Token ='1967246442:AAEuMFRGo4Hoy0nhDKF5elXLv0j9MaGB4_E'
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def First(message):
    bot.send_message(message.chat.id,rf"Команды, для отметки: {obj_keys}")

@bot.message_handler(commands=obj_keys)
def Marking(message):
    createxl.create_xl()
    fb_data=createxl.mark_xl(message.from_user.username,str(message.text[1 :len(message.text)]))
    print(fb_data, "Фидбек")
    bot.send_message(message.chat.id, str("Сохранено. ")+ str( fb_data[2])+" "+ str(fb_data[3]))

@bot.message_handler(commands=['таблица'])
def таблица(message):
    bot.send_document(message.chat.id, open(rf"months//{createxl.now_month()}.xlsx", "rb"))

@bot.message_handler(commands=['start_time'])
def таблица(message):
    bot.send_message(message.chat.id, start_time)
    print(message.chat.id)
print("Bot is polling")
bot.send_message(1931633887,"Bot is polling")
bot.polling(none_stop=True)
