from django.db import models
from room.models import Room
from user.models import CustomUser


# class Assignment(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     giver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="giver")
#     receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="receiver")
#     status = models.BooleanField(default="not sent")  # or false
#
#     def __str__(self):
#         return f"Santa: {self.giver}, giftee: {self.receiver}."
    