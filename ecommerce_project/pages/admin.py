"""
Admin configuration for the pages app.
"""

from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """
    Admin interface for the Page model.

    Displays title, slug, created, and updated fields in the list view.
    """
    list_display = ['title', 'slug', 'created', 'updated']