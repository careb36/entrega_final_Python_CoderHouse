"""
User views for the ecommerce project.

This module contains views for user authentication, registration, and profile management.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from users.forms import User_registration_form
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from .models import Profile
from django.contrib.auth.models import User
from .forms import ProfileForm, User_registration_form
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import SetPasswordForm


def login_request(request):
    """
    Handle user login requests.

    Processes GET requests by displaying the login form and POST requests by
    authenticating the user and redirecting to the home page on success.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered login page or home page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {
                    'message': f'{username} Bienvenido a TIENDA !!, Encontraras tu prenda ideal!'}
                return render(request, 'home/index.html', context=context)

        return render(request, 'users/login.html', {'error': 'Usuario o contraseña incorrectas', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
        form.fields['username'].widget.attrs['class'] = 'form-control'
        form.fields['password'].widget.attrs['class'] = 'form-control'
        return render(request, 'users/login.html', {'form': form})

def register(request):
    """
    Handle user registration requests.

    Processes GET requests by displaying the registration form and POST requests by
    validating and saving the new user, then redirecting to the login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered registration page or redirect to login.
    """
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            # se agrega el mensaje de que su cuenta fue creada con exito
            messages.success(request, 'Su cuenta se ha creado con éxito')
            return redirect('login')
        else:
            context = {}
            context['form'] = form
            context['errors'] = form.errors.as_data()
        return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class View_profile(TemplateView):
    """
    View for displaying the user's profile.

    Requires login and renders the profile template with the user's profile data.
    """
    model = Profile
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        self.profile = Profile.objects.filter(user__username=user).first()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context
@method_decorator(login_required, name='dispatch')
class UpdatePasswordProfile(UpdateView):
    """
    View for updating the user's password.

    Uses a custom SetPasswordForm and redirects to the profile view on success.
    """
    model = User
    fields = ['password']
    success_url = reverse_lazy('view-profile')
    template_name = 'users/update_password.html'

    def get_object(self):
        user = User.objects.filter(username=self.request.user).first()
        return user

    def get_form(self, form_class=None):
        form = SetPasswordForm(self.request.user, self.request.POST or None)
        return form


@method_decorator(login_required, name='dispatch')
class Update_profile(UpdateView):
    """
    View for updating the user's profile information.

    Uses ProfileForm and creates a profile if it doesn't exist.
    """
    form_class = ProfileForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('view-profile')

    def get_object(self):
        # Retrieve the object to be edited
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile


class CustomLogoutView(LogoutView):
    """
    Custom logout view that adds a success message before logging out.

    Extends Django's LogoutView to provide user feedback and proper redirect.
    """
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        # Add success message before logout
        messages.success(request, 'You have been successfully logged out. Thank you for visiting EcommerceHub!')
        return super().dispatch(request, *args, **kwargs)
