from django.contrib import admin
from django.utils.html import format_html
from .models import Coach

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'age', 'is_active', 'photo_preview')
    list_filter = ('position', 'is_active')
    search_fields = ('first_name', 'last_name')
    
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'position', 'photo')
        }),
        ('Дополнительно', {
            'fields': ('birth_date', 'nationality', 'experience', 'bio')
        }),
        ('Статус', {
            'fields': ('is_active', 'order', 'join_date')
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" height="100" />', obj.photo.url)
        return "Нет фото"
    photo_preview.short_description = "Превью"