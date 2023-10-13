# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from measurement.models import Sensor


#



def create_sensor(request):
    if request.method == 'POST':
        sensor = Sensor()
        sensor.name = request.Post.get('name')
        sensor.description = request.Post.get('description')
        sensor.save()
    return HttpResponseRedirect('/')

@api_view
def demo(request):
    data={'massage':'Hello'}
    return Response(data)