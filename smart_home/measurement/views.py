# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurements
# from measurement.serializers import DemoSerializer, MeasurementsSerializer
from measurement.serializers import (SensorListSerializer,
                                     SensorDetailListSerializer,
                                     MeasurementsSerializer,
                                     MeasurementDetailListSerializer,
                                     CreateSensorSerializer)


class MeasurementsListView(generics.ListAPIView):
    '''Выводит список измерений'''
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer


class SensorListView(generics.ListAPIView):
    '''Выводит список датчиков'''
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorDetailView(APIView):
    '''Выводит один датчик по id'''
    def get(self, request ,pk):
        sensor = Sensor.objects.get(id=pk)

        serializer = SensorDetailListSerializer(sensor)
        return Response(serializer.data)


class MeasurementDetailView(generics.RetrieveAPIView):
    '''Выводит описание одного измерения по id'''
    queryset = Measurements.objects.all()
    serializer_class = MeasurementDetailListSerializer


class add_measurement(APIView):
    '''Добавляет описание измерения'''
    def post(self, request):
        serializer = MeasurementsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

class CreateSensor(APIView):
    '''Создает датчик и обновляет его'''
    def post(self, request):
        serializer = CreateSensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self,request,*args,**kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response({"error": "Method put is not allowed"})
        try:
            instance = Sensor.objects.get(pk=pk)
        except:
            return Response({"error": "Method put is not allowed"})
        serializer = CreateSensorSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})






