# admin.py
from django.contrib import admin
from .models import Coach

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'age', 'is_active')
    list_filter = ('position', 'is_active')
    search_fields = ('first_name', 'last_name')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'position', 'photo')
        }),
        ('Дополнительно', {
            'fields': ('birth_date', 'nationality', 'experience', 'bio', 'achievements')
        }),
        ('Статус', {
            'fields': ('is_active', 'order', 'join_date')
        }),
    )