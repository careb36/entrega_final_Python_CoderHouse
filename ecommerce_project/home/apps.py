from django.apps import AppConfig
"""
Home app configuration module.

This module contains the configuration for the home Django application.
"""



class HomeConfig(AppConfig):
    """
    Configuration class for the home Django application.

    This class defines the configuration settings for the home app,
    including the default auto field and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
