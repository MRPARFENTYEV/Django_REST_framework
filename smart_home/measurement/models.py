from django.db import models


class Measurements(models.Model):
    temperature =models.FloatField(max_length=5)
    created_at = models.DateTimeField(max_length=10)
    def __str__(self):
        return self.temperature
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    measurement = models.ManyToManyField(Measurements, related_name='measurement')
    def __str__(self):
        return self.name




# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
