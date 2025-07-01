from django.db import models
from django.utils import timezone

class Coach(models.Model):
    POSITION_CHOICES = [
        ('head', 'Главный тренер'),
        ('assistant', 'Ассистент'),
        ('gk', 'Тренер вратарей'),
        ('fitness', 'Тренер по физподготовке'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='coaches/', blank=True)
    join_date = models.DateField(default=timezone.now)
    achievements = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)  # Для сортировки

    class Meta:
        ordering = ['order', 'position', 'last_name']
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        if self.birth_date:
            today = timezone.now().date()
            return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        return None

    def __str__(self):
        return f"{self.full_name} ({self.get_position_display()})"