from django.urls import path
from . import views

urlpatterns = [
    path('', views.EducationalQualificationCreate.as_view()),
    path('get-all/',
         views.ApplicantEducationalQualificationGetAll.as_view()),
    path('<int:id>/', views.EducationalQualificationUpdateDelete.as_view()),
#     path('update-applicant-educational-qualification-document-by-applicant-educational-experience-id/doc/<int:Id>/',
#          views.update_applicant_educational_documents),
]
