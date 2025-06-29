from rest_framework import permissions, status, views
from rest_framework.response import Response
from .models import DriverLocation


class DriverLocationUpdateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        lat = request.data.get('lat')
        lng = request.data.get('lng')
        DriverLocation.objects.create(
            chofer=request.user,
            latitud=lat,
            longitud=lng,
        )
        return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
