from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    rut = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
