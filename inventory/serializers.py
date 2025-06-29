from rest_framework import serializers
from .models import Warehouse, CylinderType, CylinderStock

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class CylinderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CylinderType
        fields = '__all__'

class CylinderStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CylinderStock
        fields = '__all__'
