from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    sensor_id = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.CASCADE)
    temperature = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
