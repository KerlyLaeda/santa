from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import WishForm
from .models import Wish
from room.models import Room
from user.models import CustomUser


# disable editing after draw started
@login_required
def make_wish(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # Check if the user is a participant of this room
    if not room.participants.filter(id=request.user.id).exists():
        messages.warning(request, "You are not a participant of this room. Please follow the invite link in your email or create a new room.")
        return redirect("index")

    # wish, created = Wish.objects.get_or_create(user=request.user, room=room)
    wish = Wish.objects.filter(user=request.user, room=room).first()
    if request.method == "POST":
        form = WishForm(request.POST, instance=wish)
        if form.is_valid():
            form.save()
            messages.success(request, "Your wish has been saved! You can now edit it.")
            return HttpResponseRedirect(request.path_info)  # reloads
    else:
        form = WishForm(instance=wish)

    return render(request, "wish/wish.html", {
        "form": form,
        "room": room,
        "wish_exists": wish is not None
    })
