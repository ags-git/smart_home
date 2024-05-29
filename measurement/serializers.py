from rest_framework import serializers
from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class Sensor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'location']


class Measurement_serializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'value', 'time']
