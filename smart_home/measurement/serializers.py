from rest_framework import serializers
#
# data = serializers.serialize('json', self.list_sensors())
# return HttpResponse(data, content_type="application/json")
class DemoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    measurement = serializers.BooleanField()

    # temperature = serializers.FloatField()
    # created_at = serializers.DateTimeField()
class MeasurementsSerializer(serializers.Serializer):
    temperature = serializers.FloatField()
    created_at = serializers.DateTimeField()
