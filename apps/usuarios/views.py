from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import RegitrarUsuarioForm
from .models import Usuario
# Create your views here.

class RegistrarUsuarioView(CreateView):
   template_name = "registrar.html"
   form_class = RegitrarUsuarioForm
   model = Usuario
   
   def form_valid(self, form):
      messages.success(self.request, 'Registro exitoso. Inicie Sesión.')
      form.save()
      return redirect('usuarios:registrar') 

class LoginUsaurio(LoginView):
   template_name = "login.html"

   def get_success_url(self):
      messages.success(self.request, 'Login exitoso.')
      return reverse('index')
   

class LogoutUsaurio(LogoutView):
   template_name = "logout.html"
   #success_url = reverse_lazy('index')

   def get_success_url(self):
      messages.success(self.request, 'Logout exitoso.')
      return reverse('apps.usuario:logout')