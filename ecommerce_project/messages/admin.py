"""
This module configures the admin interface for the Message model.
"""

from django.contrib import admin
from .models import Message
from ecommerce.admin import admin_site

class MessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Message model.
    """
    list_display = ['sender', 'receiver', 'subject', 'sent_date', 'read']

admin_site.register(Message, MessageAdmin)