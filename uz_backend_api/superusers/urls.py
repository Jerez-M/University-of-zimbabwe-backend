from django.urls import path
from superusers import views

urlpatterns = [
    path('', views.CreateSuperuserView.as_view(), name='create_superuser'),
    path('<int:pk>/', views.SuperuserReadUpdateDestroyView.as_view()),
    path('get-all/', views.GetAllSuperusers.as_view()),
]
