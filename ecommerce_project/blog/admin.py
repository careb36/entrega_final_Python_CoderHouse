from django.contrib import admin
from .models import Blog, Category, Tag
from ecommerce.admin import admin_site

"""Admin configuration for the blog app."""

class BlogAdmin(admin.ModelAdmin):
    """Admin interface for Blog model."""
    list_display = ['title', 'author', 'published', 'created']

class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    list_display = ['name', 'slug']

class TagAdmin(admin.ModelAdmin):
    """Admin interface for Tag model."""
    list_display = ['name', 'slug']

admin_site.register(Blog, BlogAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Tag, TagAdmin)
