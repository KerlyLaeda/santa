from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from .models import Room


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ["name", "cost_limit", "currency"]

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
