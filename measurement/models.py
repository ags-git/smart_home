from django.db import models

# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.CASCADE)
    value = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
