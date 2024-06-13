from django.db import models
from accounts.models import User

# Create your models here.

class Superuser(models.Model):
    Employment_status = (
        ('FULL TIME', 'FULL TIME'),
        ('PART TIME', 'PART TIME'),
        ('CONTRACT', 'CONTRACT'),
    )
    STATUS = (
        ('ACTIVE', 'ACTIVE'),
        ('RESIGNED', 'RESIGNED'),
        ('DISMISSED', 'DISMISSED'),
        ('ON LEAVE', 'ON LEAVE'),
        ('LEFT ORGANIZATION', 'LEFT ORGANIZATION'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    employeeNumber = models.CharField(max_length=30, unique=True, blank=True, null=True)
    job_position = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, choices=STATUS)
    employment_status = models.CharField(max_length=200, blank=True, null=True, choices=Employment_status)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    