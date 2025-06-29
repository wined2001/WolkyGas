from rest_framework import serializers
from .models import CashMovement

class CashMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashMovement
        fields = '__all__'
