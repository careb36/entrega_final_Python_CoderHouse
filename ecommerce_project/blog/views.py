from django.views.generic import ListView, DetailView, CreateView, DeleteView, \
    UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .models import Blog
from .forms import BlogForm

"""Blog views for the ecommerce project."""


class BlogListView(ListView):
    """View for listing published blog posts."""
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 10

    def get_queryset(self):
        """Return queryset of published blogs ordered by creation date."""
        return Blog.objects.filter(published=True).order_by('-created')


class BlogDetailView(DetailView):
    """View for displaying a single published blog post."""
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_queryset(self):
        """Return queryset of published blogs."""
        return Blog.objects.filter(published=True)


class BlogCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new blog post."""
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        """Set the author to the current user and save the form."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for updating an existing blog post."""
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        """Check if the user is the author or a superuser."""
        blog = self.get_object()
        return self.request.user == blog.author or self.request.user.is_superuser


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting a blog post."""
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        """Check if the user is the author or a superuser."""
        blog = self.get_object()
        return self.request.user == blog.author or self.request.user.is_superuser


class BlogSearchView(TemplateView):
    """View for searching blog posts."""
    template_name = 'blog/blog_search.html'

    def get_context_data(self, **kwargs):
        """Add search results and pagination to the context."""
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            # Filter blogs by title or content containing the query, and only published ones
            blogs = Blog.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query),
                published=True
            ).order_by('-created')
            paginator = Paginator(blogs, 10)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['blogs'] = page_obj
            context['query'] = query
        return context





