from django.db import models
from companies.models import Company
from accounts.models import User
from orders.models import Order


class CashMovement(models.Model):
    INCOME = 'ingreso'
    OUTCOME = 'egreso'
    TYPE_CHOICES = [
        (INCOME, 'Ingreso'),
        (OUTCOME, 'Egreso'),
    ]

    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    motivo = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    chofer = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto}"
