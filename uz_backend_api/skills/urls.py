from django.urls import path
from skills import views

urlpatterns = [
    path('', views.CreateSkillView.as_view(), name='create_Skill'),
    path('<int:pk>/', views.SkillReadUpdateDestroyView.as_view()),
    path('get-all-by-institution-id/<int:institution_id>', views.GetAllSkillsByInstitutionId.as_view()),
    path('get-all/', views.GetAllSkills.as_view()),
]
