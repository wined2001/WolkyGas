from django.contrib import admin
from .models import CashMovement

@admin.register(CashMovement)
class CashMovementAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'monto', 'fecha', 'chofer', 'company')
    list_filter = ('tipo', 'company')
    search_fields = ('motivo',)
