"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# from smart_home import views.demo 'этот вариант не работает
from measurement.views import (SensorListView, SensorDetailView, MeasurementsListView,MeasurementDetailView,
                               CreateSensor,add_measurement)

urlpatterns = [
    # path(' ', views.demo), 'этот тоже
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),  # подключаем маршруты из приложения measurement
    # path('demo/', include('measurement.urls')),
    path('list_sensors/', SensorListView.as_view()), # просмотреть все датчики
    path('SensorDetailView/<int:pk>/', SensorDetailView.as_view()),# посмотреть детальную информацию по датчику( указать id)
    path('MeasurementsSerializer/', MeasurementsListView.as_view()),# просмотреть все датчики измерения
    path('MeasurementDetailView/<int:pk>/',MeasurementDetailView.as_view()),# просмотреть детальную информацию по измерению ( указать id)
    path('CreateSensor/',CreateSensor.as_view()),# добавить датчик
    path('UpdateSensor/<int:pk>/',CreateSensor.as_view()),# обновить датчик
    path('add_measurements/', add_measurement.as_view()) # добавить измерения


    # path('create_sensor/',create_sensor)
]
