"""
URL configuration for the pages app.
"""

from django.urls import path
from .views import PageDetailView

# URL patterns for the pages app
urlpatterns = [
    path('<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
]