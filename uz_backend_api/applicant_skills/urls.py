from django.urls import path
from applicant_skills import views

urlpatterns = [
    path('', views.CreateApplicantSkillView.as_view(), name='create_ApplicantSkill'),
    path('<int:pk>/', views.ApplicantSkillReadUpdateDestroyView.as_view()),
    path('get-all-by-institution-id/<int:institution_id>', views.GetAllApplicantSkillsByInstitutionId.as_view()),
    path('get-all-by-applicant-id/<int:applicant_id>', views.GetAllApplicantSkillsByApplicantId.as_view()),
    path('get-all/', views.GetAllApplicantSkills.as_view()),
]
