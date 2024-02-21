from django.db import models
from job_categories.models import JobCategory
from institution.models import Institution

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, help_text='Enter the job title')
    description = models.TextField(null=True, blank=True, help_text='Provide a detailed description of the job')
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, null=True, blank=True, help_text='Select the job category')
    company_name = models.CharField(max_length=255, blank=True, null=True, help_text='Enter the company name')
    location = models.CharField(null=True, blank=True, max_length=255, help_text='Enter the job location')
    requirements = models.TextField(null=True, blank=True, help_text='Enter the job requirements')
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text='Enter the job salary')
    posted_date = models.DateField(blank=True, null=True, help_text='Enter the date the job was posted')
    deadline = models.DateField(blank=True, null=True, help_text='Enter the deadline date for the job')

    def __str__(self):
        return f'{self.title}'