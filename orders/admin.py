from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'cliente_nombre', 'estado', 'forma_pago', 'tipo_cilindro', 'chofer', 'company'
    )
    list_filter = ('estado', 'forma_pago', 'company')
    search_fields = ('cliente_nombre', 'direccion')
