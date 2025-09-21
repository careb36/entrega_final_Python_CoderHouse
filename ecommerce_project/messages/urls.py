"""
This module defines URL patterns for the messages app.
"""

from django.urls import path
from .views import MessageInboxView, MessageSentView, MessageDetailView, MessageCreateView, MessageDeleteView

# URL patterns for the messages app
urlpatterns = [
    path('inbox/', MessageInboxView.as_view(), name='message_inbox'),
    path('sent/', MessageSentView.as_view(), name='message_sent'),
    path('<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('compose/', MessageCreateView.as_view(), name='message_compose'),
    path('<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]