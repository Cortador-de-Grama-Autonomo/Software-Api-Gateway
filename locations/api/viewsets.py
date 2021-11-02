from rest_framework.viewsets import ModelViewSet
from locations.models import Locations
from .serializers import LocationsSerializer

class LocationsViewSet(ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer