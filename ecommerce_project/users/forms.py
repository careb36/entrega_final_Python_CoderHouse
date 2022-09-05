from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from .models import Profile

class User_registration_form(UserCreationForm):
    email=forms.EmailField(required=True)
    password1= forms.CharField(label='Password',widget=forms.PasswordInput)
    password2= forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password1', 'password2')
        help_texts={k:'' for k in fields}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'imagen', 'description', 'url']
        widgets = {
            'name': forms.TextInput(),
            'surname':forms.TextInput(),
            'description':forms.Textarea(),
            'url': forms.URLInput(),
        }

class SetPasswordForm(SetPasswordForm):
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
    
