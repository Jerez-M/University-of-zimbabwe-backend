from django.db import models
from accounts.models import User


OPERATION_CHOICES = (
    ('CREATE', 'CREATE'),
    ('UPDATE', 'UPDATE'),
    ('DELETE', 'DELETE'),
)


class AuditTrail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operation = models.CharField(max_length=255, choices=OPERATION_CHOICES, null=True, blank=True)
    action = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    model_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "audit_trail"
        verbose_name_plural = "Audit Trails"

    def __str__(self):
        return self.action
