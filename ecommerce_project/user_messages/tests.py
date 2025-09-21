"""Tests for the user_messages app."""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Message


class MessageModelTest(TestCase):
    """Test cases for the Message model."""
    def setUp(self):
        """Set up test data for Message model tests."""
        self.sender = User.objects.create_user(username='sender', password='12345')
        self.receiver = User.objects.create_user(username='receiver', password='12345')

    def test_message_creation(self):
        """Test creating a message and its string representation."""
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            subject='Test Subject',
            content='Test content'
        )
        self.assertEqual(message.subject, 'Test Subject')
        self.assertEqual(str(message), f'Message from {self.sender} to {self.receiver}: Test Subject')


class MessageViewTest(TestCase):
    """Test cases for message views."""
    def setUp(self):
        """Set up test data for view tests."""
        self.client = Client()
        self.sender = User.objects.create_user(username='sender', password='12345')
        self.receiver = User.objects.create_user(username='receiver', password='12345')
        self.message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            subject='Test Subject',
            content='Test content'
        )

    def test_message_inbox_view_unauthenticated(self):
        """Test that unauthenticated users are redirected from inbox."""
        response = self.client.get(reverse('message_inbox'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_message_inbox_view_authenticated(self):
        """Test that authenticated users can access inbox."""
        self.client.login(username='receiver', password='12345')
        response = self.client.get(reverse('message_inbox'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Subject')

    def test_message_detail_view_permission_denied(self):
        """Test that unauthorized users cannot access message details."""
        other_user = User.objects.create_user(username='other', password='12345')
        self.client.login(username='other', password='12345')
        response = self.client.get(reverse('message_detail', kwargs={'pk': self.message.pk}))
        self.assertEqual(response.status_code, 403)

    def test_message_create_view_authenticated(self):
        """Test creating a message via POST."""
        self.client.login(username='sender', password='12345')
        response = self.client.post(reverse('message_create'), {
            'receiver': self.receiver.pk,
            'subject': 'New Subject',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to inbox
        self.assertTrue(Message.objects.filter(subject='New Subject').exists())


class MessageFormTest(TestCase):
    """Test cases for message forms."""
    def setUp(self):
        """Set up test data for form tests."""
        self.sender = User.objects.create_user(username='sender', password='12345')
        self.receiver = User.objects.create_user(username='receiver', password='12345')

    def test_message_form_valid(self):
        """Test valid message form submission."""
        from .forms import MessageForm
        form = MessageForm(data={
            'receiver': self.receiver.pk,
            'subject': 'Valid Subject',
            'content': 'Valid content longer than 5 characters'
        })
        form.sender = self.sender
        self.assertTrue(form.is_valid())

    def test_message_form_invalid_subject(self):
        """Test form validation for invalid subject."""
        from .forms import MessageForm
        form = MessageForm(data={
            'receiver': self.receiver.pk,
            'subject': 'Hi',  # Too short
            'content': 'Valid content longer than 5 characters'
        })
        form.sender = self.sender
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors)

    def test_message_form_invalid_content(self):
        """Test form validation for invalid content."""
        from .forms import MessageForm
        form = MessageForm(data={
            'receiver': self.receiver.pk,
            'subject': 'Valid Subject',
            'content': 'Hi'  # Too short
        })
        form.sender = self.sender
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)