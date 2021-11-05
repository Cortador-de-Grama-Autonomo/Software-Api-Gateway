from rest_framework.serializers import ModelSerializer
from base.models import GrassMachine

class GrassMachineSerializer(ModelSerializer):
    class Meta:
        model = GrassMachine
        fields = ['id', 'name', 'serie_number', 'battery_percentage', 'model', 'power', 'voltage', 'motor_type', 'cut_type', 'rotation_number', 'qr_code_identifier', 'owner']