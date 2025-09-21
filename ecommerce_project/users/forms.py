"""
Forms for the users app.

This module defines forms for user registration, profile management, and password updates.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from .models import Profile


class User_registration_form(UserCreationForm):
    """
    Form for user registration.

    Extends UserCreationForm to include email validation and custom password fields.
    """
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k: '' for k in fields}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with this email already exists.')
        return email


class ProfileForm(forms.ModelForm):
    """
    Form for editing user profile information.

    Includes validation to strip HTML tags from text fields.
    """

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'imagen', 'description', 'url']
        widgets = {
            'name': forms.TextInput(),
            'surname': forms.TextInput(),
            'description': forms.Textarea(),
            'url': forms.URLInput(),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            return strip_tags(name)
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if surname:
            return strip_tags(surname)
        return surname

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description:
            return strip_tags(description)
        return description


class SetPasswordForm(SetPasswordForm):
    """
    Form for setting a new password.

    Extends Django's SetPasswordForm with custom Meta fields.
    """

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

'''
class Profile_form(forms.ModelForm):
    name= forms.CharField(label='Nombre')
    surname= forms.CharField(label='Apellido')
    image=forms.ImageField(required=False)
    description=forms.CharField(label='Description', widget=forms.TextInput)
    url=forms.URLField(required=False)
    class Meta:
        model = Profile
        fields=('name','surname','image','description','url')
'''
    
