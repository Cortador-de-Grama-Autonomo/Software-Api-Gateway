from rest_framework.serializers import ModelSerializer
from base.models import GrassMachine

class GrassMachineSerializer(ModelSerializer):
    class Meta:
        model = GrassMachine
        fields = ['id', 'model', 'qr_code_identifier', 'description', 'owner']