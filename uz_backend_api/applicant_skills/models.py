from django.db import models
from applicants.models import Applicant
from skills.models import Skill
# Create your models here.

class ApplicantSkill(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, help_text='Select the user')
    skills = models.ManyToManyField(Skill, help_text='Select the skill')
    # proficiency_level = models.CharField(max_length=255, null=True, blank=True, help_text='Enter the proficiency level')