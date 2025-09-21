"""
URL configuration for the ecommerce project.

This module defines the main URL patterns for the Django application,
routing requests to appropriate app views and serving static/media files.
"""

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from .admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),  # Admin interface
    path('', include('home.urls')),  # Home page and main landing
    path('pages/', include('blog.urls')),  # Blog-related pages
    path('pages/', include('pages.urls')),  # Static pages
    path('comments/', include('comments.urls')),  # Comment management
    path('messages/', include('user_messages.urls')),  # User messaging system
    path('accounts/', include('users.urls')),  # User authentication and profiles
    path('ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor file uploads
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
