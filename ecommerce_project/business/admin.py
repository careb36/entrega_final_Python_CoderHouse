from django.contrib import admin
from sre_parse import Verbose
from tabnanny import verbose
from business.models import Stores, Opinions

@admin.register(Stores)
class Stores_admin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number', 'schedules']

@admin.register(Opinions)
class Opinions_admin(admin.ModelAdmin):
    list_display = ['name', 'calification', 'comment']




