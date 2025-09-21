"""
App configuration for the comments app.

This module defines the configuration for the Django comments application.
"""

from django.apps import AppConfig


class BusinessConfig(AppConfig):
    """
    Configuration for the comments Django app.

    Sets the default auto field and specifies the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
