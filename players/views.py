from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer

class PlayerListCreateView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer