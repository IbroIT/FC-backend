from rest_framework import serializers
from .models import Player, Career, Achievement  # Исправленный импорт

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['club', 'years']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['title']

class PlayerSerializer(serializers.ModelSerializer):
    careers = CareerSerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)
    
    class Meta:
        model = Player
        fields = '__all__'