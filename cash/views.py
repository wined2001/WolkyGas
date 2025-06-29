from rest_framework import viewsets, permissions
from .models import CashMovement
from .serializers import CashMovementSerializer

class CashMovementViewSet(viewsets.ModelViewSet):
    queryset = CashMovement.objects.all()
    serializer_class = CashMovementSerializer
    permission_classes = [permissions.IsAuthenticated]
