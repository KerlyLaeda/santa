from django.urls import path
from . import views


urlpatterns = [
    path("<int:room_id>/", views.make_wish, name="make_wish"),
]

