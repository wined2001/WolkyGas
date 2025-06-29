from django.db import models
from accounts.models import User


class DriverLocation(models.Model):
    chofer = models.ForeignKey(User, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chofer} @ {self.timestamp}"
