from django.db import models
from institution.models import Institution

# Create your models here.

class Skill(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True, help_text='Enter the skill name')
    description = models.TextField(blank=True, null=True, help_text='Enter a description of the skill')