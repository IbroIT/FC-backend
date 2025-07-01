from django.contrib import admin

# Register your models here.
# academy/admin.py
from django.contrib import admin
from .models import AcademyPlayer

@admin.register(AcademyPlayer)
class AcademyPlayerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position', 'number', 'is_active')
    list_filter = ('position', 'is_active', 'join_year')
    search_fields = ('first_name', 'last_name', 'number')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'position', 'number', 'photo')
        }),
        ('Детали', {
            'fields': ('birth_date', 'height', 'weight', 'join_year')
        }),
        ('Статистика', {
            'fields': ('matches', 'goals', 'assists', 'rating')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )