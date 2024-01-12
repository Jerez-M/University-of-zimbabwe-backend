from django.urls import path
from administrators import views

urlpatterns = [
    path('', views.CreateAdministratorView.as_view(), name='administrator'),
    path('<int:pk>/', views.AdministratorReadUpdateDestroyView.as_view()),
    path('get-all/', views.GetAllAdministrators.as_view()),
]
