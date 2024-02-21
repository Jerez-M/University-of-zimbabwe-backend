from rest_framework.serializers import ModelSerializer
from .models import Job

class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

        extra_kwargs = {
            "job_category": {"required": True},
            "titile": {"required": True},
            "deadline": {"required": True},
            "posted_date": {"required": True},
        }


class JobRetrieveSerializer(ModelSerializer):    
    class Meta:
        model = Job
        fields = "__all__"
        depth = 1