from django.urls import path

from .views import RegistrarUsuarioView, LoginUsuario,LogoutUsuario, PreLogoutUsuario

app_name='usuarios'

urlpatterns  = [
   path('registrar/',RegistrarUsuarioView.as_view(), name="registrar"),
   path('login/',LoginUsuario.as_view(), name="login"),
   path('prelogout/',PreLogoutUsuario.as_view(), name="prelogout"),
   path('logout/',LogoutUsuario.as_view(), name="logout"),
]