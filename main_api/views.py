from _datetime import datetime, timedelta

from pytz import timezone as tz

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from main_api.models import Weather, City
from main_api.serializers import WeatherSerializer, GetWeatherSerializer
from main_api.utils import get_weather, set_weather


class WeatherView(viewsets.ModelViewSet):

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class GetWeatherView(APIView):

    def get(self, request):
        serializer = GetWeatherSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        data_request = serializer.validated_data

        weather = Weather.objects.filter(city_id__name=data_request['city']).order_by('-last_date')
        data_response = weather.values().first()
        city_coordinates = City.objects.filter(name=data_request['city']).values().first()
        if not data_response:
            try:
                weather_data = get_weather(city_coordinates['lat'], city_coordinates['lon'])
                set_weather(data_request['city'], weather_data)
                data_response = weather.values().first()
            except TypeError:
                return Response({'error': 'Город не найден'})

        diff = datetime.now().replace(tzinfo=tz('UTC')) - data_response['last_date']
        if diff > timedelta(minutes=30):
            weather_data = get_weather(city_coordinates['lat'], city_coordinates['lon'])
            set_weather(data_request['city'], weather_data)

        ser = WeatherSerializer(data=data_response)
        ser.is_valid(raise_exception=True)
        response = ser.validated_data

        return Response(response)
