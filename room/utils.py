import random

from django.conf import settings
from django.core.mail import send_mail
from wish.models import Wish


def send_invitation(room, recipient_list):
    """
    Sends invitation emails with a unique link to join a room.

    :param room: Room object
    :param recipient_list: List of recipient email addresses
    """
    subject = f"You are invited to join the room {room.name}"
    invitation_link = f"{settings.SITE_URL}{room.get_invitation_link()}"
    message = f"""
    Hi there,
    
    You have been invited to join the room {room.name}. Click the link below to join:
    
    {invitation_link}
    
    Best regards,
    The Secret Santa Team
    """

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list,
        fail_silently=False,
    )


def draw(room):
    """
    Randomly assigns Secret Santas to gift receivers.

    :param room: Room object
    """
    participants = list(room.participants.all())
    random.shuffle(participants)

    # Ensure no self-assignments
    for i, giver in enumerate(participants):
        receiver = participants[(i + 1) % len(participants)]
        wish = Wish.objects.get(user=giver, room=room)
        wish.assigned_to = receiver
        wish.save()

    room.draw_started = True
    room.save()


def notify_participants(room):
    """
    Sends notification emails with the name of the assigned receiver.

    :param room: Room object
    """
    for wish in Wish.objects.filter(room=room):
        send_mail(
            subject="Your Secret Santa Assignment",
            message=f"Hi, {wish.user.first_name}, \n\n"
                    f"You have been assigned to be the Secret Santa for {wish.assigned_to.first_name} {wish.assigned_to.last_name}!\n\n"
                    f"Happy gifting!\n\n"
                    f"Best regards,\n\n"
                    f"The Secret Santa Team",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[wish.user.email],
        )
