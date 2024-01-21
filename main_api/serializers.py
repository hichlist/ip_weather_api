from rest_framework import serializers
from main_api.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['degree', 'pressure', 'wind_speed']


class GetWeatherSerializer(serializers.Serializer):
    city = serializers.CharField(allow_blank=True)
