# academy/apps.py
from django.apps import AppConfig

class AcademyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'academy'  # Должно совпадать с именем папки приложения