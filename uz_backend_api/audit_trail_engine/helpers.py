from .models import AuditTrail


def audit_trail(user_id, action, model, model_id, operation):
    AuditTrail.objects.create(
        user_id=user_id,
        action=action,
        model=model,
        model_id=model_id,
        operation=operation
    )
