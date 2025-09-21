"""
URL configuration for the comments app.

This module defines the URL patterns for comment-related views.
"""

from django.urls import path
from .views import add_comment

# URL patterns for comment functionality
urlpatterns = [
    path('add/<slug:blog_slug>/', add_comment, name='add_comment'),
]