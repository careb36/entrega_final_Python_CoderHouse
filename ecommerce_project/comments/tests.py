"""
Tests for the comments app.

This module contains unit tests for models, views, and forms in the comments application.
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Blog, Category
from .models import Comment


class CommentModelTest(TestCase):
    """
    Test cases for the Comment model.

    Tests comment creation and string representation.
    """
    def setUp(self):
        """
        Set up test data for CommentModelTest.

        Creates a test user, category, and blog post for use in tests.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='Test content',
            author=self.user,
            category=self.category,
            slug='test-blog',
            published=True
        )

    def test_comment_creation(self):
        """
        Test creating a comment instance.

        Verifies that a comment can be created and its string representation is correct.
        """
        comment = Comment.objects.create(
            post=self.blog,
            author=self.user,
            content='Test comment',
            rating=5
        )
        self.assertEqual(comment.content, 'Test comment')
        self.assertEqual(str(comment), f'Comment by {self.user} on {self.blog}')


class CommentViewTest(TestCase):
    """
    Test cases for comment views.

    Tests the add_comment view for authenticated and unauthenticated users.
    """
    def setUp(self):
        """
        Set up test data for CommentViewTest.

        Creates a test client, user, category, and blog post.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='Test content',
            author=self.user,
            category=self.category,
            slug='test-blog',
            published=True
        )

    def test_add_comment_unauthenticated(self):
        """
        Test that unauthenticated users are redirected when trying to add a comment.
        """
        response = self.client.post(reverse('add_comment', kwargs={'blog_slug': 'test-blog'}), {
            'content': 'Test comment',
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_add_comment_authenticated(self):
        """
        Test that authenticated users can successfully add comments.

        Verifies that a comment is created and the user is redirected.
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add_comment', kwargs={'blog_slug': 'test-blog'}), {
            'content': 'Test comment',
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)  # Redirect to blog detail
        self.assertTrue(Comment.objects.filter(content='Test comment').exists())


class CommentFormTest(TestCase):
    """
    Test cases for comment forms.

    Tests form validation for valid and invalid comment data.
    """
    def test_comment_form_valid(self):
        """
        Test that the comment form accepts valid data.
        """
        from .forms import CommentForm
        form_data = {
            'content': 'Valid comment content',
            'rating': 4
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_content(self):
        """
        Test that the comment form rejects content that is too short.
        """
        from .forms import CommentForm
        form_data = {
            'content': 'Hi',  # Too short
            'rating': 4
        }
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
