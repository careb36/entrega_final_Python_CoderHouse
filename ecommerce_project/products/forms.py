from distutils.command.upload import upload
from random import choices
from tkinter import Widget
from django import forms
from django.forms import ModelForm

from .models import Products


class Forms_products(forms.ModelForm):
    choices = [('S', 'S'), ('M', 'M'), ('L', 'L'),
               ('XL', 'XL'), ('XXL', 'XXL')]
    size = forms.ChoiceField(choices=choices)

    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'stock', 'size', 'available', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
        }
    
class Forms_category(forms.Form):
    name = forms.CharField(max_length=50)

