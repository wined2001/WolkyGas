from rest_framework import serializers
from .models import DriverLocation

class DriverLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLocation
        fields = '__all__'
