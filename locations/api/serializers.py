from rest_framework.serializers import ModelSerializer
from locations.models import Locations

class LocationsSerializer(ModelSerializer):
    class Meta:
        model = Locations
        fields = ['id', 'name', 'description', 'latitude', 'longitude']