from django.db import models
from institution.models import Institution

# Create your models here.

class JobCategory(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, help_text='Enter the name of the job category')
    description = models.TextField(blank=True, null=True, help_text='Provide a detailed description of the job category')

    def __str__(self):
        return f'{self.name}'
