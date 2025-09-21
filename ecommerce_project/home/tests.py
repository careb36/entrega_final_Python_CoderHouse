from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.models import Blog, Category
"""
Home app tests module.

This module contains unit tests for the home application views.
"""



class HomeViewTest(TestCase):
    """
    Test case for home view functions.

    This class contains tests for the index view, including scenarios
    with no blogs, with published blogs, and with unpublished blogs.
    """
    def setUp(self):
        """
        Set up test fixtures before each test method.

        Creates a test client, user, and category for use in tests.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category', slug='test-category')

    def test_index_view_no_blogs(self):
        """
        Test the index view when no blogs are present.

        Verifies that the view returns a 200 status code and includes
        the 'latest_blogs' context variable.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('latest_blogs', response.context)  # Context variable

    def test_index_view_with_blogs(self):
        """
        Test the index view when published blogs are present.

        Creates a published blog and verifies that it appears in the response.
        """
        blog = Blog.objects.create(
            title='Test Blog',
            content='Test content',
            author=self.user,
            category=self.category,
            slug='test-blog',
            published=True
        )
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')

    def test_index_view_unpublished_blogs_not_shown(self):
        """
        Test that unpublished blogs are not displayed in the index view.

        Creates an unpublished blog and verifies it does not appear in the response.
        """
        blog = Blog.objects.create(
            title='Unpublished Blog',
            content='Test content',
            author=self.user,
            category=self.category,
            slug='unpublished-blog',
            published=False
        )
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Unpublished Blog')
