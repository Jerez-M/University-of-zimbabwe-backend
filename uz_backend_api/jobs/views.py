from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobRetrieveSerializer, JobSerializer
from rest_framework import filters

# Create your views here.


class CreateJobView(CreateAPIView):
    permission_classes = []
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class JobReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class GetAllJobs(ListAPIView):
    permission_classes = []
    serializer_class = JobRetrieveSerializer
    queryset = Job.objects.all()


class GetAllJobsByJobCategory(ListAPIView):
    permission_classes = []
    serializer_class = JobRetrieveSerializer

    def get_queryset(self):
        job_category = self.kwargs["job_category"]
        queryset = Job.objects.filter(job_category_id=job_category)
        return queryset


class GetAllJobsByJobTitle(ListAPIView):
    permission_classes = []
    serializer_class = JobRetrieveSerializer

    def get_queryset(self):
        title = self.kwargs["title"]
        queryset = Job.objects.filter(title=title)


# class GetAllJobsByInstitutionId(ListAPIView):
#     permission_classes = []
#     serializer_class=JobRetrieveSerializer

#     def get_queryset(self):
#         institution_id = self.kwargs['institution_id']
#         queryset = Job.objects.filter(job_category__institution_id=institution_id)
#         return queryset


class GetAllJobsByInstitutionId(ListAPIView):
    permission_classes = []
    serializer_class = JobRetrieveSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ["-posted_date"]  # Order by the most recent date

    def get_queryset(self):
        institution_id = self.kwargs["institution_id"]
        queryset = Job.objects.filter(job_category__institution_id=institution_id)
        return queryset


class JobSearchAPIView(ListAPIView):
    permission_classes = []
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description", "location"]  # Fields to search
    ordering_fields = ["posted_date", "salary"]  # Fields to order by

    def get_queryset(self):
        queryset = Job.objects.all()

        # Apply filters based on user preferences
        location = self.request.query_params.get("location")
        if location:
            queryset = queryset.filter(location=location)

        min_salary = self.request.query_params.get("min_salary")
        if min_salary:
            queryset = queryset.filter(salary__gte=min_salary)

        experience_required = self.request.query_params.get("experience_required")
        if experience_required:
            queryset = queryset.filter(experience_required__lte=experience_required)

        is_featured = self.request.query_params.get("is_featured")
        if is_featured:
            queryset = queryset.filter(is_featured=is_featured)

        return queryset
