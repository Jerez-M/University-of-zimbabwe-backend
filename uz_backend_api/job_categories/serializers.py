from rest_framework.serializers import ModelSerializer
from .models import JobCategory
from institution.serializers import MinimizedInstitutionSerializer

class JobCategorySerializer(ModelSerializer):
    class Meta:
        model = JobCategory
        fields = "__all__"

        extra_kwargs = {
            "institution": {"required": True},
            "name": {"required": True}
        }


class JobCategoryRetrieveSerializer(ModelSerializer):
    institution = MinimizedInstitutionSerializer()
    
    class Meta:
        model = JobCategory
        fields = "__all__"