from django.db import models

# Create your models here.
class Game(models.Model):
    room_creator = models.TextField()
    game_opponent = models.TextField()
    game_over = models.BooleanField()
    room_name = models.TextField()

    def __str__(self):
        return self.room_name + " created by " + self.room_creator
    