from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
