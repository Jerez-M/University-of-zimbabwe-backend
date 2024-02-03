from django.db import models
from accounts.models import User

# Create your models here.

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='applicant_profile_pictures', blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

class EducationalQualification(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, blank=True, null=True)
    institution_attended = models.CharField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    file = models.FileField(upload_to='applicant_educational_documents', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.applicant.user.first_name} {self.applicant.user.lastName}'


class ApplicantWorkExperience(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, blank=True, null=True)
    employer = models.CharField(max_length=200, blank=True, null=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    job_description = models.TextField(max_length=500, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    reference_contacts_1 = models.TextField(max_length=500, blank=True, null=True)
    reference_contacts_2 = models.TextField(max_length=500, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.applicant.user.first_name} {self.applicant.user.lastName}'


class ApplicantPersonalDocument(models.Model):
    APPLICANT_PERSONAL_DOCUMENTS_TYPES = (
        ('RESUME', 'RESUME'),
        ('CV', 'CV'),
        ('IDENTIFICATION', 'IDENTIFICATION'),
        ('EDUCATIONAL', 'EDUCATIONAL')
    )
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, blank=True, null=True)
    doc_type = models.CharField(max_length=200, blank=True, null=True, choices=APPLICANT_PERSONAL_DOCUMENTS_TYPES)
    file = models.FileField(upload_to='applicant_documents', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.id}'
