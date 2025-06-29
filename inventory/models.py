from django.db import models
from companies.models import Company


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CylinderType(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    capacity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class CylinderStock(models.Model):
    cylinder_type = models.ForeignKey(CylinderType, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cylinder_type} - {self.warehouse}"
