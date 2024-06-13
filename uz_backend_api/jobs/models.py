from django.db import models
from job_categories.models import JobCategory
from institution.models import Institution

# Create your models here.

class Job(models.Model):
    LOCATION=(
        ('ONSITE', 'ONSITE'),
        ('REMOTE', 'REMOTE'),
        ('HYBRID', 'HYBRID'),
    )
    title = models.CharField(max_length=255, null=True, blank=True, help_text='Enter the job title')
    description = models.TextField(null=True, blank=True, help_text='Provide a detailed description of the job')
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, null=True, blank=True, help_text='Select the job category')
    company_name = models.CharField(max_length=255, blank=True, null=True, help_text='Enter the company name')
    job_site = models.CharField(null=True, blank=True, max_length=255, help_text='Enter the job location')
    location = models.CharField(choices=LOCATION, null=True, blank=True, max_length=255, help_text='Enter the job location')
    requirements = models.TextField(null=True, blank=True, help_text='Enter the job requirements')
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text='Enter the job salary')
    posted_date = models.DateField(blank=True, null=True, help_text='Enter the date the job was posted')
    deadline = models.DateField(blank=True, null=True, help_text='Enter the deadline date for the job')
    application_email = models.EmailField(blank=True, null=True, help_text='Enter the email address for job applications')
    application_link = models.URLField(blank=True, null=True, help_text='Enter the link for job applications')
    experience_required = models.PositiveIntegerField(blank=True, null=True, help_text='Enter the required years of experience')
    education_requirements = models.CharField(max_length=255, blank=True, null=True, help_text='Enter the education requirements')
    is_featured = models.BooleanField(default=False, help_text='Specify if the job is featured')


    def __str__(self):
        return f'{self.title}'