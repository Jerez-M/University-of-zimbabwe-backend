from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicantPersonalDocumentCreate.as_view()),
     path('<int:pk>/', views.ApplicantPersonalDocumentUpdateGetDeleteByID.as_view()),
    path('get-all/',
         views.ApplicantPersonalDocumentGetAll.as_view()),
    # path('upload-personal-documents-by-applicant-id/doc/<int:Id>/', views.update_staff_personal_document),

]
