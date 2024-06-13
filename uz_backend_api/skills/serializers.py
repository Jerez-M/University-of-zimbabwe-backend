from rest_framework.serializers import ModelSerializer
from .models import Skill
from institution.serializers import MinimizedInstitutionSerializer

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

        extra_kwargs = {
            "institution": {"required": True},
            "name": {"required": True}
        }


class SkillRetrieveSerializer(ModelSerializer):
    institution = MinimizedInstitutionSerializer()
    
    class Meta:
        model = Skill
        fields = "__all__"

class MinimizedSkillRetrieveSerializer(ModelSerializer):    
    class Meta:
        model = Skill
        fields = ['id', 'name']