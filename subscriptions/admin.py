from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('company', 'activa', 'inicio', 'vencimiento')
    list_filter = ('activa',)
    search_fields = ('company__name',)
