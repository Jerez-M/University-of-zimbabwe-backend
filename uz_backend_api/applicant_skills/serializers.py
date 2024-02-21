from rest_framework.serializers import ModelSerializer
from .models import ApplicantSkill

class ApplicantSkillSerializer(ModelSerializer):
    class Meta:
        model = ApplicantSkill
        fields = "__all__"

        extra_kwargs = {
            "applicant": {"required": True},
            "skill": {"required": True}
        }


class ApplicantSkillRetrieveSerializer(ModelSerializer):
    
    class Meta:
        model = ApplicantSkill
        fields = "__all__"