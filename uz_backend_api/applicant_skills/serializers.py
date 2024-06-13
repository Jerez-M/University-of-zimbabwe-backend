from rest_framework.serializers import ModelSerializer
from .models import ApplicantSkill
from skills.serializers import MinimizedSkillRetrieveSerializer

class ApplicantSkillSerializer(ModelSerializer):
    class Meta:
        model = ApplicantSkill
        fields = "__all__"

        extra_kwargs = {
            "applicant": {"required": True},
            "skills": {"required": True}
        }


class ApplicantSkillRetrieveSerializer(ModelSerializer):
    skills = MinimizedSkillRetrieveSerializer(many=True)
    class Meta:
        model = ApplicantSkill
        fields = "__all__"