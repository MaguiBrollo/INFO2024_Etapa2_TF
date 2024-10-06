from django.urls import path

from django.contrib.auth import views as auth_views

from .views import RegistrarUsuarioView

app_name="usuarios"

urlpatterns  = [
   path("registrar/",RegistrarUsuarioView.as_view(), name="registrar"),
   path("login/",auth_views.LoginView.as_view(), name="login")
]