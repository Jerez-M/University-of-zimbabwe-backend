from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicantWorkExperienceCreate.as_view()),
    path('get-all/', views.ApplicantWorkExperienceGetAll.as_view()),
    path('<int:pk>/', views.ApplicantWorkExperienceGetUpdateDeleteByID.as_view()),
]
