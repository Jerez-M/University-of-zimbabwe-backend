from django.urls import path
from applicants import views

urlpatterns = [
    path('', views.CreateApplicantView.as_view(), name='create_applicant'),
    path('<int:pk>/', views.ApplicantReadUpdateDestroyView.as_view()),
    path('get-all/', views.GetAllApplicants.as_view()),

    # path('update-applicant-profile-picture-using-applicant-id/<int:Id>/', views.Update_staff_profile_picture.as_view()),
]
