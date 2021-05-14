from django.db import models


class Game(models.Model):

    title = models.CharField(
        max_length=50,
        unique=True)
    description = models.TextField()
    year_released = models.PositiveIntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    time_units = models.CharField(
        max_length=8)
    age_recomendation = models.PositiveIntegerField()
    
