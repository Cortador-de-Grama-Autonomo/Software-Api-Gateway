from rest_framework.viewsets import ModelViewSet
from base.models import GrassMachine
from .serializers import GrassMachineSerializer

class GrassMachineViewSet(ModelViewSet):
    queryset = GrassMachine.objects.all()
    serializer_class = GrassMachineSerializer