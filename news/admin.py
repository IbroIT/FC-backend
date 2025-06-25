from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FootballNews

@admin.register(FootballNews)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_featured', 'is_live')
    list_filter = ('is_featured', 'is_live')
    search_fields = ('title', 'content')
    prepopulated_fields = {'excerpt': ('title',)}