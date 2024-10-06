from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import views as auth_views

from .forms import RegitrarUsuarioForm

# Create your views here.

class RegistrarUsuarioView(FormView):
   template_name = "registrar.html"
   form_class = RegitrarUsuarioForm
   success_url = reverse_lazy ("apps.usuarios:login")

   def form_valid(self, form):
      messages.success(self.request, 'Registro exitoso. Inicie Sesión.')
      form.save()
      return redirect('apps.usuarios:registrar')
   

class LoginUsaurio(LoginView):
   template_name = "login.html"

   def get_success_url(self):
      messages.success(self.request, 'Login exitoso.')

      return reverse('apps.usuario:login')
   

class LogoutUsaurio(LogoutView):
   template_name = "logout.html"
   #success_url = reverse_lazy('index')

   def get_success_url(self):
      messages.success(self.request, 'Logout exitoso.')

      return reverse('apps.usuario:logout')