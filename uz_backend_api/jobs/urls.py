from django.urls import path
from jobs import views

urlpatterns = [
    path('', views.CreateJobView.as_view(), name='create_Job'),
    path('<int:pk>/', views.JobReadUpdateDestroyView.as_view()),
    path('get-all-by-institution-id/<int:institution_id>', views.GetAllJobsByInstitutionId.as_view()),
    path('get-all-by-job-category/<int:job_category>', views.GetAllJobsByJobCategory.as_view()),
    path('get-all-by-job-title/<str:title>', views.GetAllJobsByJobTitle.as_view()),
    path('get-all/', views.GetAllJobs.as_view()),
]
