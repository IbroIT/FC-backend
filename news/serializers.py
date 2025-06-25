from rest_framework import serializers
from .models import FootballNews

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballNews
        fields = '__all__'