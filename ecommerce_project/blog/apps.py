from django.apps import AppConfig

"""Blog app configuration."""


class ProductsConfig(AppConfig):
    """Configuration for the blog app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
