from rest_framework import viewsets, permissions
from rest_framework.response import Response
from orders.models import Order


class ReportViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Placeholder: aggregated report by company
        company = request.user.company
        orders = Order.objects.filter(company=company)
        total = orders.count()
        return Response({'total_orders': total})
