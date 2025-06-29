from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response
from .models import DriverLocation
from .serializers import DriverLocationSerializer

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


class DriverLocationViewSet(viewsets.ModelViewSet):
    queryset = DriverLocation.objects.all()
    serializer_class = DriverLocationSerializer
    permission_classes = [permissions.IsAuthenticated]
