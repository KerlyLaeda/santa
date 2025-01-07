from django.db import models
from room.models import Room
from user.models import CustomUser


class Wish(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    wish = models.TextField()

    def __str__(self):
        return self.wish[:30]
