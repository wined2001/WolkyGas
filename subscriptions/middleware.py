from django.utils import timezone
from django.http import HttpResponseForbidden
from .models import Subscription


class SubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.company:
            try:
                sub = Subscription.objects.get(company=request.user.company)
                if sub.vencimiento < timezone.now().date() or not sub.activa:
                    return HttpResponseForbidden("Suscripción vencida")
            except Subscription.DoesNotExist:
                return HttpResponseForbidden("Sin suscripción")
        return self.get_response(request)
