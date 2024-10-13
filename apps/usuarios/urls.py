from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import RegistrarUsuarioView, LoginUsuarioView,LogoutUsuarioView
from .views import PreLogoutUsuarioView, EditarUsuarioView

app_name='usuarios'

urlpatterns  = [
   path('registrar/',RegistrarUsuarioView.as_view(), name="registrar"),
   path('login/',LoginUsuarioView.as_view(), name="login"),
   path('prelogout/',login_required(PreLogoutUsuarioView.as_view()), name="prelogout"),
   path('logout/',login_required(LogoutUsuarioView.as_view()), name="logout"),
   path('editar/',EditarUsuarioView, name="editar"),
]