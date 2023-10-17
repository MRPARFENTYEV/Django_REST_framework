from django.db import models


class Measurements(models.Model):
    temperature =models.FloatField(max_length=5)
    created_at = models.DateTimeField(max_length=10)
    def __str__(self):
        return self.temperature
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    # measurement = models.ManyToManyField(Measurements, related_name='measurement')
    measurement = models.ManyToManyField(Measurements, related_name='measurement') # To do: тут надо сделать foreignkey
    # def __init__(self, name, description):
    #     super().__init__()
    #     self.name = name
    #     self.description = description
    def __str__(self):
        return self.name

class MeasurementSensor(models.Model):
    measurements = models.ForeignKey(Measurements, on_delete=models.CASCADE, related_name='scopes')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='scopes')


