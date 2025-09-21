"""
Tests for the pages app.
"""

from django.test import TestCase, Client
from django.urls import reverse
from .models import Page


class PageModelTest(TestCase):
    """
    Test cases for the Page model.
    """
    def test_page_creation(self):
        """
        Test that a Page instance can be created and has correct attributes.
        """
        page = Page.objects.create(
            title='Test Page',
            content='Test content',
            slug='test-page'
        )
        self.assertEqual(page.title, 'Test Page')
        self.assertEqual(str(page), 'Test Page')


class PageViewTest(TestCase):
    """
    Test cases for the Page views.
    """

    def setUp(self):
        """
        Set up test data for view tests.
        """
        self.client = Client()
        self.page = Page.objects.create(
            title='Test Page',
            content='Test content',
            slug='test-page'
        )

    def test_page_detail_view(self):
        """
        Test that the page detail view returns 200 for an existing page.
        """
        response = self.client.get(reverse('page_detail', kwargs={'slug': 'test-page'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Page')

    def test_page_detail_view_not_found(self):
        """
        Test that the page detail view returns 404 for a non-existent page.
        """
        response = self.client.get(reverse('page_detail', kwargs={'slug': 'nonexistent'}))
        self.assertEqual(response.status_code, 404)