# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coach

class CoachStatsAPIView(APIView):
    def get(self, request):
        stats = {
            'total': Coach.objects.count(),
            'by_position': dict(Coach.objects.values_list('position')
                               .annotate(count=models.Count('id'))),
            'active': Coach.objects.filter(is_active=True).count(),
        }
        return Response(stats)