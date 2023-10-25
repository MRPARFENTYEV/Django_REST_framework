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


#
# data1 = {'name':'esg1',
#             'description':'descriptiones'}

# @api_view(['POST'])
# def create_sensor(request):
#     if request.method == 'POST':
#         sensor = Sensor()
#         sensor.name = request.Post.GET.get('name')
#         sensor.description = request.Post.GET.get('description')
#         sensor.save()
#         print(request)
#         return Response('Модель создана')
# @api_view(['GET'])
# def list_sensors(request):
#     sens = Sensor.objects.all()
#     measur = Measurements.objects.all()
#     ser = DemoSerializer(sens, many=True)
#     mes = MeasurementsSerializer(measur, many=True)
#     return Response([ser.data, mes.data])

# @api_view(['POST'])
# def create_sensor(request):
#     if request.method == 'POST':
#         req = str(request).split('/')[-1].split('=')[-1]
#         name = request.Post('name')
#         # name = request.Post.get('name',APPEND_SLASH=False)
#         return Response(req)

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
    #
    # def get_2(self, request ,pk):
    #     mes = Measurements.objects.get(id=pk)
    #     serializer = MeasurementDetailListSerializer(mes)
    #     return Response(serializer.data)
# class SensorDetailListView(generics.RetrieveAPIView):
    # queryset = Sensor.objects.all()
    # serializer_class = SensorDetailListSerializer


class MeasurementDetailView(generics.RetrieveAPIView):
    '''Выводит описание ондного измерения по id'''

    # def get(self, request ,pk):
        # sensor = Sensor.objects.get(id=pk)
        # serializer = SensorDetailListSerializer(sensor)
        # return Response(serializer.data)

    queryset = Measurements.objects.all()
    serializer_class = MeasurementDetailListSerializer

    # sens = Sensor.objects.all()
    # measur = Measurements.objects.all()
    # ser = DemoSerializer(sens, many=True)
    # mes = MeasurementsSerializer(measur, many=True)
class CreateSensor(APIView):
    def post(self, request):
        create_sensor = CreateSensorSerializer(data=request.data)
        if create_sensor.is_valid():
            create_sensor.save()
        return Response(status=201)



