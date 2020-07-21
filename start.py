#!/usr/bin/env python3

import os
import sys
import json
import time
import telebot
import requests

from telebot import types

# Set start dirs
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from other import MainConfig

# initialization bot
config = MainConfig()
bot = telebot.TeleBot(token=config.telegram_token)


@bot.message_handler(commands=['start', 'help'])
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

    api_url = f'http://api.page2images.com/restfullink' \
              f'?p2i_url={message.text}' \
              f'&p2i_key={config.p2i_token}' \
              f'&p2i_size={config.size}' \
              f'&p2i_screen={config.size}' \
              f'&p2i_quality={config.quality}'

    while True:
        try:
            response = requests.get(api_url, timeout=15)

            if response.status_code == 200:
                data = json.loads(response.content.decode())

                if data['status'] == 'processing':
                    time.sleep(5)
                    continue

                elif data['status'] == 'error':
                    bot.send_message(message.chat.id, 'API-сервер не может обработать URL, проверь его правильность ☝')
                    break

                elif data['status'] == 'finished':
                    photo_url = data['image_url']
                    bot.send_photo(message.chat.id, photo_url)
                    break

            else:
                bot.send_message(message.chat.id, 'В данный момент я не могу сделать скриншот, попробуй позже 😔')
                break

        except Exception as e:
            bot.send_message(message.chat.id, 'API-сервер недоступен, попробуй позже 😔')
            print('Page2Images error:', e)
            break


bot.polling()
