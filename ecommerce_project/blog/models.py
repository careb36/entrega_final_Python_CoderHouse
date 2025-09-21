from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

"""Blog models for the ecommerce project."""

class Category(models.Model):
    """Model representing a blog category."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        app_label = 'blog'

    def __str__(self):
        """Return the string representation of the category."""
        return self.name

class Tag(models.Model):
    """Model representing a blog tag."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        app_label = 'blog'

    def __str__(self):
        """Return the string representation of the tag."""
        return self.name

class Blog(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        app_label = 'blog'

    def __str__(self):
        """Return the string representation of the blog post."""
        return self.title
