"""
Models for the pages app.
"""

from django.db import models


class Page(models.Model):
    """
    Model representing a static page in the application.

    Attributes:
        title (CharField): The title of the page.
        content (TextField): The content of the page.
        slug (SlugField): A unique slug for URL generation.
        created (DateTimeField): The date and time when the page was created.
        updated (DateTimeField): The date and time when the page was last updated.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return the title of the page as its string representation.
        """
        return self.title