from rest_framework import serializers
from .models import Peak


class PeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peak
        fields = ['id', 'name', 'lat', 'lon', 'altitude']
