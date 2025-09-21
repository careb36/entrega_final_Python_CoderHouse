"""Models for the user_messages app."""

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """Model representing a private message between users."""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the message."""
        return f'Message from {self.sender} to {self.receiver}: {self.subject}'