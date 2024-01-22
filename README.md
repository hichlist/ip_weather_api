# Сервис погоды

Сервис погоды передает текущие показатели для заданного города России через API или Telegram Bot

## Requirements

- Python 3.8
- Django 3.2
- Django Rest Framework 3.14
- Aiogram 2.25.2

## Installation
- pip install -r requirements.txt
- python3 manage.py migrate
- python3 manage.py loaddata fixtures/initial.json --app app.city
- Создать файл .env и поместить туда ключи от телеграм бота и яндекс API
с именами TELEGRAM_TOKEN и YA_TOKEN соответственно.

## Start
- python3 manage.py runserver
- python3 main_api/bot.py