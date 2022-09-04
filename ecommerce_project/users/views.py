from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import User_registration_form, Profile_form
from django.contrib import messages
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.models import User

# Create your views here.

def login_request(request):
    if request.method=='POST':
        form= AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                context={'message' :f'{username} Bienvenido a TIENDA !!, Encontraras tu prenda ideal!'}
                return render (request, 'home/index.html',context=context)     
        
        return render(request,'users/login.html',{'error': 'Usuario o contraseña incorrectas','form':form})
    
    elif request.method=='GET':
        form=AuthenticationForm()
        return render (request,'users/login.html',{'form':form})

def register(request):
    if request.method=='POST':
        form=User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Su cuenta se ha creado con éxito') # se agrega el mensaje de que su cuenta fue creada con exito
            return redirect('login')
        
        form= User_registration_form
        context={'form':form}
        if form.errors:
            print('error',form.errors)
        return render(request, 'users/register.html',context)

    elif request.method=='GET':
        form=User_registration_form()
        return render(request,'users/register.html',{'form':form})


class View_profile(TemplateView):
    model = User
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        self.users = User.objects.filter(username=user)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = self.users
        return context

class Update_profile(UpdateView):
        model = User
        fields = '__all__'
        success_url = '/users/profile/'
        template_name = 'users/update_profile.html'

# PERFILES
def create_profile(request):
    if request.method=='POST':
         form=Profile_form(request.POST)
         if form.is_valid():
             form.save()
             return render (request, 'home/index.html',context=context)  
        

    elif request.method == 'GET':
         form = Profile_form()
         context = {'form':form}
         return render(request, 'users/new_profile.html', context=context)
     
