from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import JobCategory
from .serializers import JobCategoryRetrieveSerializer, JobCategorySerializer

# Create your views here.

class CreateJobCategoryView(CreateAPIView):
    permission_classes = []
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()

class JobCategoryReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class=JobCategorySerializer
    queryset = JobCategory.objects.all()

class GetAllJobCategories(ListAPIView):
    permission_classes = []
    serializer_class=JobCategoryRetrieveSerializer
    queryset = JobCategory.objects.all()
  

class GetAllJobCategoriesByInstitutionId(ListAPIView):
    permission_classes = []
    serializer_class=JobCategoryRetrieveSerializer

    def get_queryset(self):
        institution_id = self.kwargs['institution_id']
        queryset = JobCategory.objects.filter(institution_id=institution_id)
        return queryset