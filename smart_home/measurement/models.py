from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    # measurements = models.ForeignKey(Measurements, related_name='measurements', on_delete=models.CASCADE)
    # measurement = models.ManyToManyField(Measurements, related_name='measurement')
    # measurement = models.OneToMany(Measurements,related_name='measurement')
    # measurement = models.ForeignKey(Measurements,on_delete=models.CASCADE, related_name='measurement') # To do: тут надо сделать foreignkey

    def __str__(self):
        return self.name

class Measurements(models.Model):
    temperature =models.FloatField(max_length=5)
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor,related_name='measurements', on_delete= models.CASCADE)


    def __str__(self):
        return  self.temperature

    # return str([self.temperature, self.created_at])







# class MeasurementSensor(models.Model):
#     measurements = models.ForeignKey(Measurements, on_delete=models.CASCADE, related_name='scopes')
#     sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='scopes')


