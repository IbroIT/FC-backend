from django.shortcuts import render

# Create your views here.
# academy/views.py
from django.shortcuts import render, get_object_or_404
from .models import AcademyPlayer

def academy_players(request):
    players = AcademyPlayer.objects.filter(is_active=True).order_by('number')
    return render(request, 'academy/players_list.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(AcademyPlayer, pk=pk)
    return render(request, 'academy/player_detail.html', {'player': player})