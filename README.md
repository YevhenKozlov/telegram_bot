# Тестовое задание

Телеграм бот, который отвечает за создание скриншотов web-стриниц на основе URL.
Для запуска данного програмного продукта необходимо:
1. Установить Python 3.6 (либо выше).
2. Установить зависимости выполнив команду `pip3 install -r requirements.txt`.
3. Настроить конфигурационный файл `configs/main.ini`:
```ini
[MAIN]

# string (TelegramBot token)
telegram_token = your_token

# string (Page2Images token)
p2i_token = your_token

# integer (0 - 100)
quality = ...

# string (example: 1920x1080)
size = ...
```

Для запуска необходимо выполнить: `sudo python3 start.py`.
