from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Skill
from .serializers import SkillRetrieveSerializer, SkillSerializer

# Create your views here.

class CreateSkillView(CreateAPIView):
    permission_classes = []
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

class SkillReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class=SkillSerializer
    queryset = Skill.objects.all()

class GetAllSkills(ListAPIView):
    permission_classes = []
    serializer_class=SkillRetrieveSerializer
    queryset = Skill.objects.all()
  

class GetAllSkillsByInstitutionId(ListAPIView):
    permission_classes = []
    serializer_class=SkillRetrieveSerializer

    def get_queryset(self):
        institution_id = self.kwargs['institution_id']
        queryset = Skill.objects.filter(institution_id=institution_id)
        return queryset