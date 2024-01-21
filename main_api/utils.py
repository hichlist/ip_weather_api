from datetime import datetime as dt
from os import environ
from pytz import timezone as tz
import requests
from dotenv import find_dotenv, load_dotenv

from main_api.models import Weather, City
from weather.settings import YA_WEATHER_LINK

env_path = find_dotenv()
load_dotenv(env_path)

def get_weather(lat: float, lon: float):
    data = requests.get(f'{YA_WEATHER_LINK}?lat={lat}&lon={lon}&lang=ru_RU',
                        headers={'X-Yandex-API-Key': environ['YA_TOKEN'],
                                 'content-type': 'application/json'})
    return data.json()['fact']


def set_weather(city: str, data: dict):
    get_city = City.objects.get(name=city)
    weather = Weather.objects.create(city_id=get_city, degree=data['temp'], pressure=data['pressure_mm'],
                                     wind_speed=data['wind_speed'], last_date=dt.now().replace(tzinfo=tz('UTC')))
    weather.save()
