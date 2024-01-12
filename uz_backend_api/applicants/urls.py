from django.urls import path
from applicants import views

urlpatterns = [
    path('', views.CreateApplicantView.as_view(), name='create_applicant'),
    path('<int:pk>/', views.ApplicantReadUpdateDestroyView.as_view()),
    path('get-all/', views.GetAllApplicants.as_view()),
]
