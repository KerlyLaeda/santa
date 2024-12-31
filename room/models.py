# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from user.models import CustomUser as User


class Room(models.Model):
    CURRENCY_CHOICES = [
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("PLN", "Polish Zloty"),
        ("GEL", "Georgian Lari"),
        # more ...
    ]

    # id? room #
    name = models.CharField(max_length=200)
    cost_limit = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")
    # cost_limit = MoneyField(max_digits=14, default_currency='USD')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name="rooms")

    def __str__(self):
        return f"Room {self.name} (admin: {self.admin.first_name} {self.admin.last_name})"

    def get_absolute_url(self):
        return reverse("room_details", kwargs={"pk": self.pk})
