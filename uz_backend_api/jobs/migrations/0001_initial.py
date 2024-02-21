# Generated by Django 5.0.1 on 2024-02-21 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Enter the job title', max_length=255, null=True)),
                ('description', models.TextField(blank=True, help_text='Provide a detailed description of the job', null=True)),
                ('company_name', models.CharField(blank=True, help_text='Enter the company name', max_length=255, null=True)),
                ('location', models.CharField(blank=True, help_text='Enter the job location', max_length=255, null=True)),
                ('requirements', models.TextField(blank=True, help_text='Enter the job requirements', null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, help_text='Enter the job salary', max_digits=10, null=True)),
                ('posted_date', models.DateField(blank=True, help_text='Enter the date the job was posted', null=True)),
                ('deadline', models.DateField(blank=True, help_text='Enter the deadline date for the job', null=True)),
                ('job_category', models.ForeignKey(blank=True, help_text='Select the job category', null=True, on_delete=django.db.models.deletion.CASCADE, to='job_categories.jobcategory')),
            ],
        ),
    ]
