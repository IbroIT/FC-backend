from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coach
from .serializers import CoachSerializer

@api_view(['GET'])
def coaches_api(request):
    coaches = Coach.objects.filter(is_active=True).order_by('order', 'position')
    serializer = CoachSerializer(coaches, many=True, context={'request': request})
    return Response(serializer.data)
