from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
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


# LOGIN

def login_request(request):
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
        return render(request, 'users/login.html', {'form': form})

# REGISTRO


def register(request):
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


# PERFIL
class View_profile(TemplateView):
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
    form_class = ProfileForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('view-profile')

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile
