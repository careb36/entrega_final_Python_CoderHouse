from sre_parse import Verbose
from tabnanny import verbose
from django.contrib import admin
from products.models import Products

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'size']

class Meta:
    Verbose_name='Product'
    Verbose_name_plural='Products'
