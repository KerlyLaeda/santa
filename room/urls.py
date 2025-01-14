from django.urls import path
from . import views


urlpatterns = [
    path("new/", views.RoomCreateView.as_view(template_name="room/create_room.html"), name="create_room"),
    path("<int:pk>/", views.RoomDetailView.as_view(template_name="room/room_details.html"), name="room_details"),
    path("invite/<uuid:token>/", views.join_room, name="room_invitation"),
    path("<int:room_id>/invite/", views.invite, name="invite"),
    path("<int:room_id>/start_draw/", views.start_draw, name="start_draw"),
]
