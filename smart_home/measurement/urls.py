from django.urls import path
from measurement.views import create_sensor, list_sensors, demo

#
urlpatterns = [
    path('demo/', demo),
    path('create_sensor/', create_sensor),
    path('list_sensors/', list_sensors)
]

