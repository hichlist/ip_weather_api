from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name='Название города', max_length=50)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Weather(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    degree = models.IntegerField(verbose_name='Температура')
    pressure = models.IntegerField(verbose_name='Атмосферное давление')
    wind_speed = models.IntegerField(verbose_name='Скорость ветра')
    last_date = models.DateTimeField(verbose_name='Последнаяя дата запроса')

    class Meta:
        verbose_name_plural = 'Weather'

    def __str__(self):
        return self.city_id.name
