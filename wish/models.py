from django.db import models
from room.models import Room
from user.models import CustomUser


class Wish(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    wish = models.TextField()
    assigned_to = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        related_name="assigned_santa",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.wish[:30]
