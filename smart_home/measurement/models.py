from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Measurements(models.Model):
    temperature =models.FloatField(max_length=5)
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor,related_name='measurements', on_delete= models.CASCADE)

    def __str__(self):
        return  self.temperature

