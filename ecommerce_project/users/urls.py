
"""
URL patterns for the users app.

This module defines the URL routes for user-related views such as login, registration,
profile management, and password updates.
"""

from django.urls import path
from .views import login_request, register, View_profile, Update_profile, UpdatePasswordProfile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', register, name='signup'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', View_profile.as_view(), name='view-profile'),
    path('profile/update/', Update_profile.as_view(), name='update-profile'),
    path('profile/password/update/', UpdatePasswordProfile.as_view(), name='update-password'),
]
