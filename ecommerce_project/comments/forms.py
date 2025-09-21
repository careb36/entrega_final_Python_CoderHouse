"""
Forms for the comments app.

This module defines form classes for handling comment submissions,
including validation and cleaning of user input.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for creating and editing comments.

    Uses ModelForm to automatically generate fields from the Comment model,
    with custom widgets and validation for content.
    """
    class Meta:
        model = Comment
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_content(self):
        """
        Clean and validate the content field.

        Ensures content is provided and meets minimum length requirements.
        Strips HTML tags for security.

        Returns:
            str: The cleaned content.

        Raises:
            ValidationError: If content is empty or too short.
        """
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('Content is required.')
        if len(content) < 5:
            raise ValidationError('Content must be at least 5 characters long.')
        return strip_tags(content)