from django.urls import path

from django.contrib.auth import views as auth_views

from .views import RegistrarUsuarioView, Login

app_name='usuarios'

urlpatterns  = [
   path('registrar/',RegistrarUsuarioView.as_view(), name="registrar"),
   path('login/',Login.as_view(), name="login")
]