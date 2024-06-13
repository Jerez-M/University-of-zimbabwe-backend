# Generated by Django 5.0.1 on 2024-03-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_application_email_job_application_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_remote',
        ),
        migrations.AddField(
            model_name='job',
            name='job_site',
            field=models.CharField(blank=True, help_text='Enter the job location', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, choices=[('ONSITE', 'ONSITE'), ('REMOTE', 'REMOTE'), ('HIBRID', 'HIBRID')], help_text='Enter the job location', max_length=255, null=True),
        ),
    ]