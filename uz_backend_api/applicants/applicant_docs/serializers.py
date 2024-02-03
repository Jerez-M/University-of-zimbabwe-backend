from rest_framework import serializers
from ..models import ApplicantPersonalDocument


class ApplicantPersonalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantPersonalDocument
        exclude = ['date_created', 'last_updated']


