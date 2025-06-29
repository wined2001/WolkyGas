from django.contrib import admin
from .models import Warehouse, CylinderType, CylinderStock

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'company')
    search_fields = ('name',)

@admin.register(CylinderType)
class CylinderTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'capacity')
    search_fields = ('name',)

@admin.register(CylinderStock)
class CylinderStockAdmin(admin.ModelAdmin):
    list_display = ('cylinder_type', 'warehouse', 'quantity', 'company')
    list_filter = ('company',)
