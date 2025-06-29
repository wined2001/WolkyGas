"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import ReportViewSet
from geolocation.views import DriverLocationUpdateView, DriverLocationViewSet
from accounts.views import UserViewSet
from companies.views import CompanyViewSet
from inventory.views import (
    WarehouseViewSet,
    CylinderTypeViewSet,
    CylinderStockViewSet,
)
from orders.views import OrderViewSet
from cash.views import CashMovementViewSet
from subscriptions.views import SubscriptionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"companies", CompanyViewSet)
router.register(r"warehouses", WarehouseViewSet)
router.register(r"cylinder-types", CylinderTypeViewSet)
router.register(r"cylinder-stocks", CylinderStockViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"cash-movements", CashMovementViewSet)
router.register(r"subscriptions", SubscriptionViewSet)
router.register(r"locations", DriverLocationViewSet)
router.register(r"reports", ReportViewSet, basename="report")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/location/", DriverLocationUpdateView.as_view(), name="location"),
    path("api/", include(router.urls)),
]
