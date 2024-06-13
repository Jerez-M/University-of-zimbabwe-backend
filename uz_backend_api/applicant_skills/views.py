from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import ApplicantSkill
from .serializers import ApplicantSkillRetrieveSerializer, ApplicantSkillSerializer

# Create your views here.

class CreateApplicantSkillView(CreateAPIView):
    permission_classes = []
    serializer_class = ApplicantSkillSerializer
    queryset = ApplicantSkill.objects.all()

class ApplicantSkillReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class=ApplicantSkillSerializer
    queryset = ApplicantSkill.objects.all()

class GetAllApplicantSkills(ListAPIView):
    permission_classes = []
    serializer_class=ApplicantSkillRetrieveSerializer
    queryset = ApplicantSkill.objects.all()
  

class GetAllApplicantSkillsByInstitutionId(ListAPIView):
    permission_classes = []
    serializer_class=ApplicantSkillRetrieveSerializer

    def get_queryset(self):
        institution_id = self.kwargs['institution_id']
        queryset = ApplicantSkill.objects.filter(skills__institution_id=institution_id)
        return queryset
    
class GetAllApplicantSkillsByApplicantId(ListAPIView):
    permission_classes = []
    serializer_class=ApplicantSkillRetrieveSerializer

    def get_queryset(self):
        applicant_id = self.kwargs['applicant_id']
        queryset = ApplicantSkill.objects.filter(applicant_id=applicant_id)
        return queryset