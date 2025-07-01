from django.urls import path
from . import views

urlpatterns = [
    path('', views.coaches_list, name='coaches-list'),  # это HTML
    path('api/', views.coaches_api, name='coaches-api'),  # это JSON
]
