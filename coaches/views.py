from django.shortcuts import render
from .models import Coach

def coaches_list(request):
    coaches = Coach.objects.filter(is_active=True).order_by('order', 'position')
    return render(request, 'coaches/list.html', {'coaches': coaches})

def coach_detail(request, pk):
    coach = Coach.objects.get(pk=pk)
    return render(request, 'coaches/detail.html', {'coach': coach})