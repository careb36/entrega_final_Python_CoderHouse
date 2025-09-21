"""Forms for the user_messages app."""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from .models import Message


class MessageForm(forms.ModelForm):
    """Form for creating and editing messages."""
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'content']
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        """Initialize the form with sender to exclude from receiver choices."""
        self.sender = kwargs.pop('sender', None)
        super().__init__(*args, **kwargs)
        # Exclude sender from receiver choices
        if self.sender:
            self.fields['receiver'].queryset = self.fields['receiver'].queryset.exclude(id=self.sender.id)

    def clean_subject(self):
        """Validate and clean the subject field."""
        subject = self.cleaned_data.get('subject')
        if not subject:
            raise ValidationError('Subject is required.')
        if len(subject) < 3:
            raise ValidationError('Subject must be at least 3 characters long.')
        return strip_tags(subject)

    def clean_content(self):
        """Validate and clean the content field."""
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('Content is required.')
        if len(content) < 5:
            raise ValidationError('Content must be at least 5 characters long.')
        return strip_tags(content)