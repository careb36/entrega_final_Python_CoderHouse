from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Blog, Category, Tag

"""Tests for the blog app."""


class BlogModelTest(TestCase):
    """Tests for blog models."""
    def setUp(self):
        """Set up test data for model tests."""
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.tag = Tag.objects.create(name='Test Tag', slug='test-tag')

    def test_blog_creation(self):
        """Test creating a blog post."""
        blog = Blog.objects.create(
            title='Test Blog',
            content='Test content',
            author=self.user,
            category=self.category,
            slug='test-blog'
        )
        blog.tags.add(self.tag)
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(str(blog), 'Test Blog')

    def test_category_str(self):
        """Test the string representation of a category."""
        self.assertEqual(str(self.category), 'Test Category')

    def test_tag_str(self):
        """Test the string representation of a tag."""
        self.assertEqual(str(self.tag), 'Test Tag')


class BlogViewTest(TestCase):
    """Tests for blog views."""
    def setUp(self):
        """Set up test data for view tests."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.superuser = User.objects.create_superuser(username='admin', password='12345')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.tag = Tag.objects.create(name='Test Tag', slug='test-tag')
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='Test content',
            author=self.user,
            category=self.category,
            slug='test-blog',
            published=True
        )
        self.blog.tags.add(self.tag)

    def test_blog_list_view(self):
        """Test the blog list view."""
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')

    def test_blog_detail_view(self):
        """Test the blog detail view."""
        response = self.client.get(reverse('blog_detail', kwargs={'slug': 'test-blog'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')

    def test_blog_create_view_unauthenticated(self):
        """Test blog create view for unauthenticated user."""
        response = self.client.get(reverse('blog_create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_blog_create_view_authenticated(self):
        """Test blog create view for authenticated user."""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('blog_create'))
        self.assertEqual(response.status_code, 200)

    def test_blog_update_view_permission_denied(self):
        """Test blog update view permission denied for other user."""
        other_user = User.objects.create_user(username='other', password='12345')
        self.client.login(username='other', password='12345')
        response = self.client.get(reverse('blog_update', kwargs={'slug': 'test-blog'}))
        self.assertEqual(response.status_code, 403)

    def test_blog_delete_view_permission_denied(self):
        """Test blog delete view permission denied for other user."""
        other_user = User.objects.create_user(username='other', password='12345')
        self.client.login(username='other', password='12345')
        response = self.client.get(reverse('blog_delete', kwargs={'slug': 'test-blog'}))
        self.assertEqual(response.status_code, 403)


class BlogFormTest(TestCase):
    """Tests for blog forms."""
    def setUp(self):
        """Set up test data for form tests."""
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.tag = Tag.objects.create(name='Test Tag', slug='test-tag')

    def test_blog_form_valid(self):
        """Test valid blog form."""
        from .forms import BlogForm
        form_data = {
            'title': 'Valid Title',
            'content': 'Valid content longer than 10 characters',
            'category': self.category.id,
            'tags': [self.tag.id],
            'published': True
        }
        form = BlogForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blog_form_invalid_title(self):
        """Test blog form with invalid title."""
        from .forms import BlogForm
        form_data = {
            'title': 'Hi',  # Too short
            'content': 'Valid content longer than 10 characters',
            'category': self.category.id,
            'tags': [self.tag.id],
            'published': True
        }
        form = BlogForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_blog_form_invalid_content(self):
        """Test blog form with invalid content."""
        from .forms import BlogForm
        form_data = {
            'title': 'Valid Title',
            'content': 'Hi',  # Too short
            'category': self.category.id,
            'tags': [self.tag.id],
            'published': True
        }
        form = BlogForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
