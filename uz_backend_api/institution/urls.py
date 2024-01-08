from django.urls import path
from institution import views

urlpatterns = [
    path('', views.CreateInstitutionView.as_view(), name='create_institution'),
    path('<int:pk>/', views.InstitutionReadUpdateDestroyView.as_view()),
    path('get-all-institutions/', views.GetAllInstitutions.as_view()),
    # path('get-institution-logo/<int:institutionId>/', views.GetInstitutionLogo.as_view()),
    # path('update-institution-logo/<int:institutionId>/', views.update_institution_logo),
]
