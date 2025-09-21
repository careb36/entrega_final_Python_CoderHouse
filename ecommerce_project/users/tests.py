"""
Tests for the users app.

This module contains unit tests for models, views, and forms in the users application.
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile


class ProfileModelTest(TestCase):
    """
    Tests for the Profile model.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_profile_creation(self):
        """
        Test that a Profile is automatically created for a new User.
        """
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.name, '')


class UserViewTest(TestCase):
    """
    Tests for user-related views.
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='12345')

    def test_login_request_get(self):
        """
        Test GET request to login view.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_request_post_valid(self):
        """
        Test POST request to login view with valid credentials.
        """
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 200)  # Renders home/index.html

    def test_login_request_post_invalid(self):
        """
        Test POST request to login view with invalid credentials.
        """
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrong'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Usuario o contraseña incorrectas')

    def test_register_get(self):
        """
        Test GET request to register view.
        """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_post_valid(self):
        """
        Test POST request to register view with valid data.
        """
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_view_profile_unauthenticated(self):
        """
        Test access to profile view without authentication.
        """
        response = self.client.get(reverse('view-profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_view_profile_authenticated(self):
        """
        Test access to profile view with authentication.
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('view-profile'))
        self.assertEqual(response.status_code, 200)


class UserFormTest(TestCase):
    """
    Tests for user-related forms.
    """

    def test_user_registration_form_valid(self):
        """
        Test User_registration_form with valid data.
        """
        from .forms import User_registration_form
        form_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'password123',
            'password2': 'password123'
        }
        form = User_registration_form(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_registration_form_invalid_email_duplicate(self):
        """
        Test User_registration_form with duplicate email.
        """
        User.objects.create_user(username='existing', email='test@example.com', password='12345')
        from .forms import User_registration_form
        form_data = {
            'username': 'newuser',
            'email': 'test@example.com',  # Duplicate
            'password1': 'password123',
            'password2': 'password123'
        }
        form = User_registration_form(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_profile_form_valid(self):
        """
        Test ProfileForm with valid data.
        """
        from .forms import ProfileForm
        form_data = {
            'name': 'Test Name',
            'surname': 'Test Surname',
            'description': 'Test description',
            'url': 'http://example.com'
        }
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())
