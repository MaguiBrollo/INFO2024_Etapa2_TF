from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from django.contrib.auth import views as auth_views

from .forms import RegitrarUsuarioForm

# Create your views here.

class RegistrarUsuarioView(FormView):
   template_name = "templates/registrar.html"
   form_class = RegitrarUsuarioForm
   success_url = reverse_lazy ("appps.usuarios:login")

   def form_valid(self, form):
      form.save()
      return super().form_valid(form)
   

class Login(auth_views.LoginView):
   template_name = "templates/login.html"