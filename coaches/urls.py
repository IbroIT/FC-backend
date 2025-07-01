from django.urls import path
from . import views

urlpatterns = [
    path('', views.coaches_list, name='coaches-list'),
    path('<int:pk>/', views.coach_detail, name='coach-detail'),
]