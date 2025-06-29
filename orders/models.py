from django.db import models
from companies.models import Company
from accounts.models import User
from inventory.models import CylinderType


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
        ('transferencia', 'Transferencia'),
    ]
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_ruta', 'En ruta'),
        ('entregado', 'Entregado'),
    ]

    cliente_nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    tipo_cilindro = models.ForeignKey(CylinderType, on_delete=models.CASCADE)
    forma_pago = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    chofer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente_nombre} - {self.estado}"
