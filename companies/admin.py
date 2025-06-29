from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'rut', 'email', 'created_at')
    search_fields = ('name', 'rut')
