from datetime import datetime as dt
from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from main_api.models import City, Weather
from main_api.utils import get_weather, set_weather


class MockYandexResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return {'fact': {'temp': -13, 'pressure_mm': 752, 'wind_speed': 2}}


class TestYandexApi(TestCase):

    @patch('requests.get', return_value=MockYandexResponse())
    def test_get_weather(self, mocked):
        self.assertEqual(get_weather(54.45, 43.33), {'temp': -13, 'pressure_mm': 752, 'wind_speed': 2})


class WeatherModelTest(TestCase):

    def setUp(self) -> None:
        City.objects.create(name='Москва', lat=54.45, lon=43.33)
        set_weather('Москва', {'temp': -13, 'pressure_mm': 752, 'wind_speed': 2})

    def test_set_weather(self):
        weather = Weather.objects.get(id=1)
        self.assertEqual(weather.degree, -13)
        self.assertEqual(weather.pressure, 752)
        self.assertEqual(weather.wind_speed, 2)


class APIWeatherTest(APITestCase):

    def setUp(self) -> None:
        self.city = City.objects.create(name='Москва', lat=54.45, lon=43.33)
        Weather.objects.create(city_id=self.city, degree=-13, pressure=752, wind_speed=2, last_date=dt.now())

    def test_api_weather(self):
        response = self.client.get('/weather?city=Москва')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'degree': -13, 'pressure': 752, 'wind_speed': 2})
