from os import environ

from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import requests
from dotenv import find_dotenv, load_dotenv

env_path = find_dotenv()
load_dotenv(env_path)

bot = Bot(token=environ['TELEGRAM_TOKEN'])
dp = Dispatcher(bot=bot)
start_msg = 'Введите город, чтобы узнать прогноз погоды'
btn_text = 'Узнать погоду'


@dp.message_handler(Text(equals=btn_text))
async def process_start_command(msg: types.Message):
    kb = [[
        types.KeyboardButton(text=btn_text)
    ]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await msg.answer(start_msg, reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def get_weather(msg: types.Message):
    r = requests.get(f'http://127.0.0.1:8000/weather?city={msg.text}')
    data = r.json()
    if 'error' in data:
        await msg.answer(data['error'])
    else:
        response = f'Температура: {data["degree"]}° С\n' \
                   f'Атмосферное давление: {data["pressure"]} мм рт.ст.\n' \
                   f'Скорость ветра: {data["wind_speed"]} м/с'
        await msg.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp)
