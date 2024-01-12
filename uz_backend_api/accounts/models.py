from django.db import models
from django.contrib.auth.models import AbstractUser
from institution.models import Institution


class User(AbstractUser):
    # exclude fields from AbstractUser
    date_joined = None
    last_login = None
    email = None

    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    ROLE = (
        ('SUPERUSER', 'SUPERUSER'),
        ('ADMIN', 'ADMIN'),
        ('GENERAL EMPLOYEE', 'GENERAL EMPLOYEE'),
        ('APPLICANT', 'APPLICANT'),
    )
    institution = models.ForeignKey(Institution, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_names = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=25, unique=True, blank=True, null=True)
    role = models.CharField(max_length=25, blank=True, null=True, choices=ROLE)
    gender = models.CharField(max_length=15, blank=True, null=True, choices=GENDER)
    institution_email = models.EmailField(blank=True, null=True)
    altEmail = models.EmailField(blank=True, null=True, help_text="personal Email apart from the company email ")
    phone_number_1 = models.CharField(max_length=25, blank=True, null=True)
    phone_number_2 = models.CharField(max_length=25, blank=True, null=True)
    national_id = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True, help_text="The date the employee was enrolled on the organisation's system")
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'institution_email'

    class Meta:
        default_related_name = 'custom_%(class)s'

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

