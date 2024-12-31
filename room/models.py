from django.contrib.auth.models import User
from django.db import models

#
# class Room(models.Model):
#     CURRENCY_CHOICES = [
#         ("USD", "US Dollar"),
#         ("EUR", "Euro"),
#         ("PLN", "Polish Zloty"),
#         ("GEL", "Georgian Lari"),
#         # more ...
#     ]
#
#     # id? room #
#     name = models.CharField(max_length=200)
#     # django-money MoneyField
#     cost_limit = models.IntegerField()
#     currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")
#     admin = models.ForeignKey(User, on_delete=models.SET_NULL)
#     participants = models.ManyToManyField(User, related_name="rooms")
#
#     def __str__(self):
#         return f"Room {self.name} (admin: {self.admin.first_name} {self.admin.last_name})"
