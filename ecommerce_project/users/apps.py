"""
App configuration for the users app.

This module defines the configuration for the Django users application.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuration for the users Django app.

    Sets the default auto field type and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
