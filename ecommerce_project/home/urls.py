from django.urls import path
from home.views import index
"""
Home app URL configuration module.

This module defines the URL patterns for the home application.
"""


urlpatterns = [
    path('', index, name='index'),
    ]