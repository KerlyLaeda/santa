from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from .models import Room
from .utils import send_invitation


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ["name", "cost_limit"]

    def form_valid(self, form):
        form.instance.admin = self.request.user
        room = form.save()

        # Add admin to the list of participants
        room.participants.add(self.request.user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("room_details", kwargs={"pk": self.object.pk})


class RoomDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Room

    def test_func(self):
        room = self.get_object()

        # Users can access only their room and not someone else's
        return self.request.user == room.admin or self.request.user in room.participants.all()


@login_required
def join_room(request, token):
    room = get_object_or_404(Room, invitation_token=token)
    if request.user not in room.participants.all():
        room.participants.add(request.user)
        messages.success(request, f"You have joined the room {room.name}")
    else:
        messages.info(request, "You are already a participant in this room.")
    return redirect("room_details", pk=room.pk)


@login_required
def invite(request, room_id):
    room = get_object_or_404(Room, id=room_id, admin=request.user)

    # Only admin can send invitations
    if request.user != room.admin:
        messages.info(request, "Only the room admin can send invitations.")
        return redirect("room_details", pk=room.pk)

    if request.method == "POST":

        # Get the list of recipients to send invitation link to
        recipient_list = request.POST.get("recipient_list")
        if not recipient_list:
            messages.info(request, "Please provide at least one email address.")
            return redirect("invite", room_id=room.id)

        # Clean email list
        recipients = [email.strip() for email in recipient_list.split(",") if email.strip()]

        if recipients:
            send_invitation(room, recipients)
            messages.success(request, f"Invitation sent to {', '.join(recipients)}")
        else:
            messages.info(request, "No valid email address provided.")
        return redirect("room_details", pk=room.id)

    return render(request, "room/room_invitation.html", {"room": room})
