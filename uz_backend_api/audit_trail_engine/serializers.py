from rest_framework.serializers import ModelSerializer

from accounts.serializers import AuditTrailUserSerializer
from .models import AuditTrail


class AuditTrailSerializer(ModelSerializer):
    user = AuditTrailUserSerializer()

    class Meta:
        model = AuditTrail
        fields = ['id', 'user', 'action', 'created_at', 'operation']
