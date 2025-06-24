from django.urls import path
from .views import PlayerListCreateView

urlpatterns = [
    path('players/', PlayerListCreateView.as_view()),
]