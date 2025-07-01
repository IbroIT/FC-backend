from rest_framework import serializers
from .models import Coach

class CoachSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    position_display = serializers.CharField(source='get_position_display')

    class Meta:
        model = Coach
        fields = [
            'id', 'name', 'position', 'position_display', 'age',
            'nationality', 'experience', 'bio', 'image', 'achievements',
            'join_date', 'is_active'
        ]

    def get_name(self, obj):
        return obj.full_name

    def get_image(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url)
        return None

    def get_age(self, obj):
        return obj.age