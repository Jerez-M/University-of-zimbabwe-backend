# Generated by Django 5.0.1 on 2024-03-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='application_email',
            field=models.EmailField(blank=True, help_text='Enter the email address for job applications', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='application_link',
            field=models.URLField(blank=True, help_text='Enter the link for job applications', null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='education_requirements',
            field=models.CharField(blank=True, help_text='Enter the education requirements', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='experience_required',
            field=models.PositiveIntegerField(blank=True, help_text='Enter the required years of experience', null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='Specify if the job is featured'),
        ),
        migrations.AddField(
            model_name='job',
            name='is_remote',
            field=models.BooleanField(default=False, help_text='Specify if the job allows remote work'),
        ),
    ]
