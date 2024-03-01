from rest_framework import serializers

from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.Serializer):
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'date']


class SensorDetailSeriaLizer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']



# TODO: опишите необходимые сериализаторы
