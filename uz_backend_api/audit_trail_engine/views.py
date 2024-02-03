from rest_framework.response import Response
from institution.models import Institution
from .models import AuditTrail
from .serializers import AuditTrailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status


class RetrieveAuditTrailsByInstitutionView(GenericAPIView):
    permission_classes = []
    serializer_class = AuditTrailSerializer
    queryset = AuditTrail.objects.all()

    def get(self, request, institution_id):
        try:
            institution = Institution.objects.get(tenant_id=institution_id)
        except Institution.DoesNotExist:
            return Response({'error': 'Institution not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            audit_trails = self.queryset.filter(user__tenant_id=institution.tenant_id).order_by('-created_at')
            serializer = AuditTrailSerializer(audit_trails, many=True)
            return Response(serializer.data)
