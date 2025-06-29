from django.db import models
from companies.models import Company


class Subscription(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    activa = models.BooleanField(default=True)
    inicio = models.DateField()
    vencimiento = models.DateField()

    def __str__(self):
        return f"{self.company} - {'Activa' if self.activa else 'Inactiva'}"
