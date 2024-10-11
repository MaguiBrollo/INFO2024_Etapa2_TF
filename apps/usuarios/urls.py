from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import RegistrarUsuarioView, LoginUsuario,LogoutUsuario, PreLogoutUsuario

app_name='usuarios'

urlpatterns  = [
   path('registrar/',RegistrarUsuarioView.as_view(), name="registrar"),
   path('login/',LoginUsuario.as_view(), name="login"),
   path('prelogout/',login_required(PreLogoutUsuario.as_view()), name="prelogout"),
   path('logout/',login_required(LogoutUsuario.as_view()), name="logout"),
]