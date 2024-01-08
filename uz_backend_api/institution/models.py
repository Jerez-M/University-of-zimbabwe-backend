from django.db import models
from .institution_number import generate_institution_number as x

class Institution(models.Model):

    INSTITUTION_TYPE_CHOICE = (
        ('UNIVERSITY', 'UNIVERSITY'),
        ('COLLEGE', 'COLLEGE'),
        ('POLYTECHNIC', 'POLYTECHNIC'),
        ('SCHOOL', 'SCHOOL'),
        ('INSTITUTE', 'INSTITUTE'),
        ('ACADEMY', 'ACADEMY'),
        ('FOUNDATION', 'FOUNDATION'),
    )
    institution_name = models.CharField(max_length=200, blank=True, null=True)
    institution_code = models.CharField(max_length=10, blank=True, default='UZ', null=True)
    institution_type = models.CharField(max_length=250, blank=True, null=True, choices=INSTITUTION_TYPE_CHOICE)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    institution_address = models.TextField(blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='institution_logos', default='institution_logos/default_logo.jpg', blank=True, null=True)
    active = models.BooleanField(default=True, help_text="active is a boolean field, can either be Tue or False")
    institution_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    founded_year = models.PositiveBigIntegerField(blank=True, null=True)
    mission_statement = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)