# academy/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.academy_players, name='academy-players'),
    path('players/<int:pk>/', views.player_detail, name='player-detail'),
]