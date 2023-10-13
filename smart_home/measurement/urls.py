from django.urls import path

from measurement.views import demo, create_sensor

#
urlpatterns = [
path ('demo/',demo)
('create_sensor', create_sensor),
#     # TODO: зарегистрируйте необходимые маршруты
]
