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
from measurement.views import create_sensor, list_sensors, demo
# from smart_home import views.demo 'этот вариант не работает
from measurement.views import demo,list_sensors, create_sensor


urlpatterns = [
    # path(' ', views.demo), 'этот тоже
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),  # подключаем маршруты из приложения measurement
    # path('demo/', include('measurement.urls')),
    path('list_sensors/', list_sensors),
    path('demo/', demo),
    path('create_sensor/',create_sensor)
]
