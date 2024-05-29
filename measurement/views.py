from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import Sensor_serializer, Measurement_serializer


# Create your views here.

class SensorView(ListModelMixin, CreateAPIView, UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = Sensor_serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SensorDetail(RetrieveAPIView, UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = Sensor_serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class MeasurementView(ListModelMixin, CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = Measurement_serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('sensor_id'))
        return serializer.save(sensor=sensor)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
