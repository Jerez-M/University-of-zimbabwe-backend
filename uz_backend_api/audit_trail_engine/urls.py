from django.urls import path
from . import views

urlpatterns = [
    path('get-all-by-institution-id/<str:institution_id>/', views.RetrieveAuditTrailsByInstitutionView.as_view())
]
