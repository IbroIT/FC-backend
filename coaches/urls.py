from django.urls import path
from . import views

urlpatterns = [
    path('', views.coaches_api, name='coaches-api'),
    path('api/', views.coaches_api, name='coaches-api'),  # JSON
]
