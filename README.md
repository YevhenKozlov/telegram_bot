# Тестовое задание

Телеграм бот, который отвечает за создание скриншотов web-стриниц на основе URL.
Для запуска данного програмного продукта необходимо:

1. Установить библиотеку wkhtmltopdf, выполнив команду - `apt-get install wkhtmltopdf` (Linux). Для установки на другие ОС посетите [Главную страницу wkhtmltopdf](https://wkhtmltopdf.org/)
2. Установить Python 3.7 (либо выше).
3. Установить зависимости выполнив команду `pip3 install -r requirements.txt`.
4. Настроить конфигурационный файл `configs/main.ini`:
```ini
[MAIN]

# string (TelegramBot token)
telegram_token = your_token
```

Для запуска бота необходимо выполнить: `python3 __main__.py`.
