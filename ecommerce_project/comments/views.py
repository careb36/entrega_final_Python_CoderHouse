"""
Views for the comments app.

This module contains view functions for handling comment-related operations,
such as adding comments to blog posts.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Comment
from .forms import CommentForm
from blog.models import Blog


@login_required
def add_comment(request, blog_slug):
    """
    Handle adding a comment to a blog post.

    This view allows authenticated users to submit comments on published blog posts.
    If the form is valid, the comment is saved and the user is redirected to the blog detail page.
    Otherwise, the form is rendered with any validation errors.

    Args:
        request (HttpRequest): The HTTP request object.
        blog_slug (str): The slug of the blog post to comment on.

    Returns:
        HttpResponse: Redirect to blog detail on success, or rendered form on GET/invalid form.
    """
    blog = get_object_or_404(Blog, slug=blog_slug, published=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', slug=blog_slug)
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment.html', {
        'form': form,
        'blog': blog
    })
