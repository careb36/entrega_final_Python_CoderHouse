"""
This module contains views for the messages app, handling inbox, sent messages,
message details, creation, and deletion.
"""

from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Message
from .forms import MessageForm


class MessageInboxView(LoginRequiredMixin, ListView):
    """
    View for displaying the user's inbox messages.
    """
    model = Message
    template_name = 'messages/inbox.html'
    context_object_name = 'messages'
    paginate_by = 10

    def get_queryset(self):
        """
        Return messages received by the current user, ordered by sent date descending.
        """
        return Message.objects.filter(receiver=self.request.user).order_by('-sent_date')


class MessageSentView(LoginRequiredMixin, ListView):
    """
    View for displaying the user's sent messages.
    """
    model = Message
    template_name = 'messages/sent.html'
    context_object_name = 'messages'
    paginate_by = 10

    def get_queryset(self):
        """
        Return messages sent by the current user, ordered by sent date descending.
        """
        return Message.objects.filter(sender=self.request.user).order_by('-sent_date')


class MessageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    View for displaying a single message detail, accessible only to sender or receiver.
    """
    model = Message
    template_name = 'messages/message_detail.html'
    context_object_name = 'message'

    def test_func(self):
        """
        Check if the current user is the sender or receiver of the message.
        """
        message = self.get_object()
        return (self.request.user == message.sender or
                self.request.user == message.receiver)

    def get(self, request, *args, **kwargs):
        """
        Handle GET request, marking the message as read if the user is the receiver.
        """
        response = super().get(request, *args, **kwargs)
        # Mark as read if user is receiver
        if self.request.user == self.object.receiver and not self.object.read:
            self.object.read = True
            self.object.save()
        return response


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new message.
    """
    model = Message
    form_class = MessageForm
    template_name = 'messages/message_form.html'
    success_url = reverse_lazy('message_inbox')

    def get_form_kwargs(self):
        """
        Pass the current user as sender to the form.
        """
        kwargs = super().get_form_kwargs()
        kwargs['sender'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """
        Set the sender of the message to the current user before saving.
        """
        form.instance.sender = self.request.user
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting a message, accessible only to sender or receiver.
    """
    model = Message
    template_name = 'messages/message_confirm_delete.html'
    success_url = reverse_lazy('message_inbox')

    def test_func(self):
        """
        Check if the current user is the sender or receiver of the message.
        """
        message = self.get_object()
        return (self.request.user == message.sender or
                self.request.user == message.receiver)