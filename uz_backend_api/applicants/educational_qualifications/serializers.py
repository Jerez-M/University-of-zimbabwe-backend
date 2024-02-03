from rest_framework import serializers
from ..models import EducationalQualification

class ApplicantEducationalQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalQualification
        exclude = ['date_created', 'last_updated']
