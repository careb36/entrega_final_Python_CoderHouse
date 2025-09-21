"""
This module contains the app configuration for the messages app.
"""

from django.apps import AppConfig


class MessagesConfig(AppConfig):
    """
    Configuration for the messages Django app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messages_app'