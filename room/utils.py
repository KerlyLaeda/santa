from django.conf import settings
from django.core.mail import send_mail


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
