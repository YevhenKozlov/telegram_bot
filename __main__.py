#!/usr/bin/env python3

import os
import sys
import imgkit
import telebot

from telebot import types

# Set start dirs
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from other import MainConfig

# initialization temp folder for picture
if not os.path.exists('temp'):
    os.mkdir('temp')

# Initialization bot-object
config = MainConfig()
bot = telebot.TeleBot(token=config.telegram_token)


@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
    """
    Reaction on start command
    """

    bot.send_message(message.chat.id, 'Привет, отправь мне ссылку на сайт, а в ответ получишь его скриншот ✨')


@bot.message_handler(content_types=['text'])
def text_message(message: types.Message):
    """
    Reaction on any text message
    """

    bot.send_message(message.chat.id, 'Подожди минутку, делаю для тебя скриншот ❤')

    try:
        imgkit.from_url(message.text, 'temp/out.jpg')
        # TODO: send photo to user

    except Exception as e:
        print('Warning:', e)
        bot.send_message(message.chat.id, 'Не могу сделать скриншот для тебя, что-то пошло не так 😔')


if __name__ == '__main__':
    bot.polling()
