from django.db import models
from django.utils import timezone

class FootballNews(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    date = models.DateField(default=timezone.now, verbose_name="Дата")
    excerpt = models.TextField(verbose_name="Краткое описание")
    content = models.TextField(verbose_name="Содержание")
    image = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL изображения")
    likes = models.PositiveIntegerField(default=0, verbose_name="Лайки")
    comments = models.PositiveIntegerField(default=0, verbose_name="Комментарии")
    is_live = models.BooleanField(default=False, verbose_name="LIVE")
    is_featured = models.BooleanField(default=False, verbose_name="Рекомендуемые")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title