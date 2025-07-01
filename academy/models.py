from django.db import models

# Create your models here.
# academy/models.py
from django.db import models
from django.utils import timezone

class AcademyPlayer(models.Model):
    POSITION_CHOICES = [
        ('goalkeeper', 'Вратарь'),
        ('defender', 'Защитник'), 
        ('midfielder', 'Полузащитник'),
        ('forward', 'Нападающий'),
    ]
    
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    position = models.CharField("Позиция", max_length=20, choices=POSITION_CHOICES)
    birth_date = models.DateField("Дата рождения")
    number = models.PositiveIntegerField("Номер", unique=True)
    image = models.ImageField(upload_to='academy_players/')
    join_year = models.PositiveIntegerField("Год в академии", default=timezone.now().year)
    is_active = models.BooleanField("В составе", default=True)
    height = models.PositiveIntegerField("Рост (см)")
    weight = models.PositiveIntegerField("Вес (кг)")
    matches = models.PositiveIntegerField("Матчи", default=0)
    goals = models.PositiveIntegerField("Голы", default=0)
    assists = models.PositiveIntegerField("Ассисты", default=0)
    rating = models.FloatField("Рейтинг", default=0.0)
    
    class Meta:
        verbose_name = "Игрок академии"
        verbose_name_plural = "Игроки академии"
        ordering = ['number']

    def __str__(self):
        return f"{self.first_name} {self.last_name} (#{self.number})"