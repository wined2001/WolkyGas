from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count
from django.views.generic import TemplateView
from orders.models import Order


class ReportViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Placeholder: aggregated report by company
        company = request.user.company
        orders = Order.objects.filter(company=company)
        total = orders.count()
        return Response({'total_orders': total})

    @action(detail=False, methods=["get"])
    def status_summary(self, request):
        """Return number of orders by status for the authenticated user's company."""
        company = request.user.company
        summary = (
            Order.objects.filter(company=company)
            .values("estado")
            .annotate(count=Count("id"))
        )
        return Response(list(summary))


class DashboardView(TemplateView):
    template_name = "reports/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        summary = Order.objects.values("estado").annotate(count=Count("id"))
        context["summary"] = list(summary)
        return context
