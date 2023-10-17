# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from measurement.models import Sensor, Measurements
from measurement.serializers import DemoSerializer, MeasurementsSerializer


#


@api_view(['POST'])
def create_sensor(request):
    if request.method == 'POST':
        sensor = Sensor()
        sensor.name = request.Post.get('name')
        sensor.description = request.Post.get('description')
        sensor.save()
        print(request)
    return Response('Модель создана')
@api_view(['GET'])
def list_sensors(request):
    sens = Sensor.objects.all()
    measur = Measurements.objects.all()
    ser = DemoSerializer(sens, many=True)
    mes = MeasurementsSerializer(measur, many=True)
    return Response([ser.data, mes.data])






