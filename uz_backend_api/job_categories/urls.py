from django.urls import path
from job_categories import views

urlpatterns = [
    path('', views.CreateJobCategoryView.as_view(), name='create_JobCategory'),
    path('<int:pk>/', views.JobCategoryReadUpdateDestroyView.as_view()),
    path('get-all-by-institution-id/<int:institution_id>', views.GetAllJobCategoriesByInstitutionId.as_view()),
    path('get-all/', views.GetAllJobCategories.as_view()),
]
