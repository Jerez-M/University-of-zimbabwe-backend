from rest_framework import serializers
from ..models import ApplicantWorkExperience

class ApplicantWorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantWorkExperience
        exclude = ['date_created', 'last_updated']

