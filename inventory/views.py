from rest_framework import viewsets, permissions
from .models import Warehouse, CylinderType, CylinderStock
from .serializers import (
    WarehouseSerializer,
    CylinderTypeSerializer,
    CylinderStockSerializer,
)

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]

class CylinderTypeViewSet(viewsets.ModelViewSet):
    queryset = CylinderType.objects.all()
    serializer_class = CylinderTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class CylinderStockViewSet(viewsets.ModelViewSet):
    queryset = CylinderStock.objects.all()
    serializer_class = CylinderStockSerializer
    permission_classes = [permissions.IsAuthenticated]
