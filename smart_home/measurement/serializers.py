from django.db.models import ForeignKey
from rest_framework import serializers


from measurement.models import Sensor, Measurements



class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        # fields = ['temperature','created_at']
        fields = '__all__'
        def create(self, validated_data):
            return Measurements.objects.create(**validated_data)


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"


class MeasurementDetailListSerializer(serializers.ModelSerializer):
    '''Выводит одну запись измерений по id'''
    sensor = SensorListSerializer(read_only=True)# работает при внешнем ключе в measurement
    class Meta:
        model = Measurements
        # exclude = ()
        fields = '__all__'
        # fields =('id','name','temperature', )

class SensorDetailListSerializer(serializers.ModelSerializer):
    '''Выводит один датччик с измерениями по id'''
    # measurements = MeasurementDetailListSerializer( read_only=True)
    # measurements = serializers.SlugRelatedField(slug_field="created_at",read_only=True, many=True)
    '''measurements = serializers.StringRelatedField(many=True)'''
    measurements = MeasurementsSerializer(read_only=True, many=True)


    class Meta:
        model = Sensor
        # exclude = ()
        fields = '__all__'
        # fields =('id','name','description','measurement','temperature','created_at')

class CreateSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
        def create(self, validated_data):
            return Sensor.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name',instance.name)
            instance.descritpion = validated_data.get('description',instance.descritpion)
            instance.save()
            return instance




