from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
class Forms_stores(forms.Form):
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=150)
    phone_number = forms.IntegerField()
    schedules = forms.CharField(max_length=100)

    
class Forms_opinions(forms.Form):
    name = forms.CharField(max_length=50)
    calification = forms.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    comment = forms.CharField(max_length=150)