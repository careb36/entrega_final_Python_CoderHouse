from django.shortcuts import render
from blog.models import Blog
"""
Home app views module.

This module contains view functions for the home application.
"""


def index(request):
    """
    Render the home page with the latest published blogs.

    Retrieves the 5 most recent published blog posts and passes them
    to the home/index.html template for rendering.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    latest_blogs = Blog.objects.filter(published=True).order_by('-created')[:5]
    context = {
        'latest_blogs': latest_blogs,
    }
    return render(request, 'home/index.html', context=context)
