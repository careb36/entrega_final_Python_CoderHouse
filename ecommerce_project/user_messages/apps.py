"""App configuration for the user_messages app."""

from django.apps import AppConfig


class MessagesConfig(AppConfig):
    """Configuration for the user_messages Django app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_messages'