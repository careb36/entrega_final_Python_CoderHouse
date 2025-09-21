from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from ckeditor.widgets import CKEditorWidget
from .models import Blog, Category, Tag

"""Blog forms for the ecommerce project."""


class BlogForm(forms.ModelForm):
    """Form for creating and editing blog posts."""
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'tags', 'published', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditorWidget(),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_title(self):
        """Validate the title field."""
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Title is required.')
        if len(title) < 5:
            raise ValidationError('Title must be at least 5 characters long.')
        return strip_tags(title)

    def clean_content(self):
        """Validate the content field."""
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('Content is required.')
        if len(content) < 10:
            raise ValidationError('Content must be at least 10 characters long.')
        return strip_tags(content)

