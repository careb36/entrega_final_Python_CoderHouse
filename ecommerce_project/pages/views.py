"""
Views for the pages app.
"""

from django.views.generic import DetailView
from .models import Page


class PageDetailView(DetailView):
    """
    View for displaying a single page detail.

    Uses Django's generic DetailView to render a page based on its slug.
    """
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'