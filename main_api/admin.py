from django.contrib import admin
from main_api.models import City, Weather

# Register your models here.

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['city_id', 'degree', 'pressure', 'wind_speed', 'last_date']
    readonly_fields = ['city_id', 'degree', 'pressure', 'wind_speed', 'last_date']
    search_fields = ['city_id']
    ordering = ['last_date']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'lat', 'lon']
    ordering = ['name']
