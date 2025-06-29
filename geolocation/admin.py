from django.contrib import admin
from .models import DriverLocation

@admin.register(DriverLocation)
class DriverLocationAdmin(admin.ModelAdmin):
    list_display = ('chofer', 'latitud', 'longitud', 'timestamp')
    list_filter = ('chofer',)
    search_fields = ('chofer__email',)
