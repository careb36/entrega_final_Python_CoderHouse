"""
Admin configuration for the comments app.

This module registers the Comment model with the Django admin site
and configures its display options.
"""

from django.contrib import admin
from .models import Comment
from ecommerce.admin import admin_site


class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for the Comment model.

    Displays key fields in the list view for easy management of comments.
    """
    list_display = ['author', 'post', 'rating', 'created']

admin_site.register(Comment, CommentAdmin)




