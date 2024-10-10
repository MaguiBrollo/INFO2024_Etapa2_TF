from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, authenticate

from .forms import RegitrarUsuarioForm, LoginForm
from .models import Usuario
# Create your views here.

class RegistrarUsuarioView(CreateView):
   template_name = "registrar.html"
   form_class = RegitrarUsuarioForm
   model = Usuario
   success_url = reverse_lazy("usuarios:login")

   def form_valid(self, form):
      messages.success(self.request, 'Registro exitoso. Ahora puede Iniciar Sesión.')
      form.save()
      return super().form_valid(form)


# USUARIOS----------------------------
class LoginUsuario(LoginView):
   template_name = "login.html"
   form_class = LoginForm
   model = Usuario
   redirect_authenticated_user =True
   
   def get_success_url(self):
      messages.success(self.request, 'Login exitoso.')
      return reverse('index')
   

class PreLogoutUsuario(TemplateView):
   template_name ='preLogout.html'
   
class LogoutUsuario(LogoutView):
   template_name = "logout.html"
   model = Usuario
   def get_success_url(self):
      messages.success(self.request, 'Logout exitoso.')
      return reverse('usuarios:logout')
   
""" 
def form_valid(self, form):
      messages.success(self.request, 'Registro exitoso. Ahora puede Iniciar Sesión.')
      usu = form.cleaned_data.get('username')
      pas = form.cleaned_data.get('password1')
      usuario = authenticate(username=usu, password=pas)
      if usuario is not None:
         form.save()
         login(self.request, usuario) 
         return reverse('index')
      else:
         return reverse('usuarios:login')
      #return super().form_valid(form) """