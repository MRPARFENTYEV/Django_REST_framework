from django.db.models import ForeignKey
from rest_framework import serializers


from measurement.models import Sensor, Measurements


#
# data = serializers.serialize('json', self.list_sensors())
# return HttpResponse(data, content_type="application/json")
class DemoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    measurement = serializers.BooleanField()


# class MeasurementsSerializer(serializers.Serializer):
#     temperature = serializers.FloatField()
#     created_at = serializers.DateTimeField()


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['temperature','created_at']



0
class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'description')



        # measurement = ForeignKey(Measurements, related_name='measurmeasurementements', on_delete=model.CASCADE) TO DO: разобраться с этой строчкой
class MeasurementDetailListSerializer(serializers.ModelSerializer):
    '''Выводит одну запись измерений по id'''
    # measurement = serializers.StringRelatedField(many=True)
    # temperature = serializers.SlugRelatedField(slug_field='temperature',many=True,read_only=True)
    # measurement = serializers.PrimaryKeyRelatedField(queryset=Measurements.objects.all())
    class Meta:
        model = Measurements
        # exclude = ()
        fields = '__all__'
        # fields =('id','name','temperature')
class SensorDetailListSerializer(serializers.ModelSerializer):
    '''Выводит один датччик с измерениями по id'''
    # measurement = serializers.StringRelatedField(many=True)
    # temperature = serializers.SlugRelatedField(slug_field='temperature',many=True,read_only=True)
    # measurement = serializers.PrimaryKeyRelatedField(queryset=Measurements.objects.all())
    temperature = MeasurementDetailListSerializer( read_only=True)
    created_at = serializers.SlugRelatedField(slug_field='created_at', read_only=True)

    class Meta:
        model = Sensor
        # exclude = ()
        # fields = '__all__'
        fields =('id','name','description','measurement','temperature','created_at')

class CreateSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields =('name','description')



