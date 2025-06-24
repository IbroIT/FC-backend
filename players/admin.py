from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Achievement, Career, Player
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def player_list(request):
    players = Player.objects.all()
    data = [{"name": p.name, "position": p.position} for p in players]
    return Response(data)

class CareerInline(admin.TabularInline):
    model = Career
    extra = 1
    fields = ('club', 'years', 'matches', 'goals', 'assists')
    readonly_fields = ('get_rating',)
    
    def get_rating(self, obj):
        return f"{obj.goals * 2 + obj.assists} pts"
    get_rating.short_description = "Рейтинг"

# Форма для редактирования достижений
class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1
    fields = ('title', 'year', 'tournament')

# Настройки для игроков основной команды
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [CareerInline, AchievementInline]
    list_display = ('name', 'number', 'position', 'age', 'matches', 'goals')
    list_filter = ('position', 'nationality')
    search_fields = ('name', 'position')
    ordering = ('number',)  # Сортировка по номеру
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'number', 'position', 'image')
        }),
        ('Статистика', {
            'fields': ('matches', 'goals', 'assists', 'rating'),
            'classes': ('collapse',)  # Сворачиваемый блок
        }),
    )

    def display_career(self, obj):
        return ", ".join([career.club for career in obj.career_set.all()])
    display_career.short_description = "Клубы"