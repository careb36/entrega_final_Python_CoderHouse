from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile

class User_registration_form(UserCreationForm):
    email=forms.EmailField(required=True, error_messages={'invalid': 'Por favor ingrese su dirección de correo electrónico'})
    password1= forms.CharField(label='Password',widget=forms.PasswordInput, error_messages={'invalid': 'Por favor ingrese un password correcto'})
    password2= forms.CharField(label='Password confirmation', widget=forms.PasswordInput, error_messages={'invalid': 'Sus passwords no coinciden'})
    #image=forms.ImageField(error_messages={'invalid': 'Por favor cargue su imagen'})
    #description=forms.Textarea(attrs={'name':'body','rows':3,'cols':2})
    #url=forms.URLField(error_messages={'invalid': 'Por favor ingrese una url correcta'})
    class Meta:
        model=User
        fields=('username','email','password1', 'password2')
        help_texts={k:'' for k in fields} 


class Profile_form(forms.ModelForm):
    name= forms.CharField(label='Nombre')
    surname= forms.CharField(label='Apellido')
    birth_date= forms.DateField(label='Fecha de nacimiento')
    address= forms.CharField(label='Direccion')

    class Meta:
        model = Profile
        fields=('name','surname','birth_date', 'address')

    
