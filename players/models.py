from django.db import models

class Player(models.Model):
    POSITION_CHOICES = [
        ('goalkeeper', 'Вратарь'),
        ('defender', 'Защитник'),
        ('midfielder', 'Полузащитник'),
        ('forward', 'Нападающий'),
    ]
    
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    positionName = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    matches = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    rating = models.FloatField()
    image = models.URLField()
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    birthDate = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
class Career(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='careers')
    club = models.CharField(max_length=100)
    years = models.CharField(max_length=50)
    matches = models.PositiveIntegerField(default=0)
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-years']  # Сортировка по годам

    def __str__(self):
        return f"{self.player.name} - {self.club} ({self.years})"
    
class Achievement(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    tournament = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
