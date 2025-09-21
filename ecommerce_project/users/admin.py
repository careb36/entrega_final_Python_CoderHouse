"""
Admin configuration for the users app.

This module registers the Profile model with the Django admin site.
"""

from django.contrib import admin
from users.models import Profile
from ecommerce.admin import admin_site


class ProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for the Profile model.

    Displays user, name, and surname in the list view.
    """
    list_display = ['user', 'name', 'surname']


admin_site.register(Profile, ProfileAdmin)

