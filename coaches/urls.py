from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.coaches_api, name='coaches-api'),  # api/ — путь для API
]
