from room.models import Room


def user_room(request):
    """A custom context processor to pass the user's room information to all templates."""
    if request.user.is_authenticated:
        room = Room.objects.filter(participants=request.user).first()
        if not room:
            room = Room.objects.filter(admin=request.user).first()
        return {"room": room}
    return {}