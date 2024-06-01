from rest_framework import serializers
from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class Sensor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'location']


class Measurement_serializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'value', 'time']

class MeasurementsList_serializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['value', 'time']

class SensorDetail_serializer(serializers.ModelSerializer):
    measurements = MeasurementsList_serializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'location', 'measurements']
