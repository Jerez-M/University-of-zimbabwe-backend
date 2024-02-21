from django.db import models
from applicants.models import Applicant
from jobs.models import Job

# Create your models here.

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, help_text='Select the job')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, help_text='Select the applicant')
    cv = models.FileField(blank=True, null=True, upload_to='resumes/', help_text='Upload the applicant\'s resume')
    cover_letter = models.TextField(blank=True, null=True, help_text='Enter the cover letter')
    application_date = models.DateTimeField(blank=True, null=True, auto_now_add=True, help_text='Date and time when the application was submitted')
    is_rejected = models.BooleanField(blank=True, null=True, default=False, help_text='Indicates if the application has been rejected') 