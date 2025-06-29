from rest_framework import viewsets, permissions
from rest_framework.response import Response
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


class DashboardView(TemplateView):
    template_name = "reports/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.company:
            company = self.request.user.company
            context["total_orders"] = Order.objects.filter(company=company).count()
        else:
            context["total_orders"] = 0
        return context
