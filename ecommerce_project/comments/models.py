"""
Models for the comments app.

This module defines the database models used in the comments application,
including the Comment model for storing user comments on blog posts.
"""

from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog


class Comment(models.Model):
    """
    Model representing a comment on a blog post.

    Attributes:
        post (ForeignKey): The blog post this comment is associated with.
        author (ForeignKey): The user who authored the comment.
        content (TextField): The text content of the comment.
        rating (IntegerField): Optional rating from 1 to 5.
        created (DateTimeField): Timestamp when the comment was created.
    """
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a string representation of the comment.

        Returns:
            str: A string showing the author and the associated blog post.
        """
        return f'Comment by {self.author} on {self.post}'
