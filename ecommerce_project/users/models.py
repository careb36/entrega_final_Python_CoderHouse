"""
User models for the ecommerce project.

This module defines the Profile model and related functionality for user profiles,
including automatic profile creation upon user registration.
"""

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_upload_to(instance, filename):
    """
    Custom upload path for profile images.

    Deletes the old image file before uploading a new one to avoid orphaned files.

    Args:
        instance: The Profile instance being updated.
        filename: The original filename of the uploaded image.

    Returns:
        str: The upload path for the image file.
    """
    old_instance = Profile.objects.get(pk=instance.pk)
    # Debug print statement
    print('oldInstanceeeee', old_instance)
    old_instance.imagen.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    """
    User profile model extending Django's User model.

    Stores additional user information such as name, surname, profile image,
    description, and personal URL.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        """
        Meta options for the Profile model.

        Orders profiles by the associated user's username.
        """
        app_label = 'users'
        ordering = ['user__username']


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    """
    Signal receiver to ensure a Profile exists for each User.

    Automatically creates a Profile instance when a new User is created.

    Args:
        sender: The model class sending the signal (User).
        instance: The User instance being saved.
        **kwargs: Additional keyword arguments from the signal.
    """
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # Debug print statement
        print("Se acaba de crear un usuario y su perfil enlazado")
