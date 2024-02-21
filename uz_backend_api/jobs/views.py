from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobRetrieveSerializer, JobSerializer

# Create your views here.

class CreateJobView(CreateAPIView):
    permission_classes = []
    serializer_class = JobSerializer
    queryset = Job.objects.all()

class JobReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class=JobSerializer
    queryset = Job.objects.all()

class GetAllJobs(ListAPIView):
    permission_classes = []
    serializer_class=JobRetrieveSerializer
    queryset = Job.objects.all()
  
class GetAllJobsByJobCategory(ListAPIView):
    permission_classes = []
    serializer_class=JobRetrieveSerializer

    def get_queryset(self):
        job_category = self.kwargs['job_category']
        queryset = Job.objects.filter(job_category_id=job_category)
        return queryset

class GetAllJobsByJobTitle(ListAPIView):
    permission_classes = []
    serializer_class=JobRetrieveSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        queryset = Job.objects.filter(title=title)

class GetAllJobsByInstitutionId(ListAPIView):
    permission_classes = []
    serializer_class=JobRetrieveSerializer

    def get_queryset(self):
        institution_id = self.kwargs['institution_id']
        queryset = Job.objects.filter(job_category__institution_id=institution_id)
        return queryset