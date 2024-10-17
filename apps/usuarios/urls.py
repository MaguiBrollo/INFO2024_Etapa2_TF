from django.urls import path, reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .views import RegistrarUsuarioView, LoginUsuarioView,LogoutUsuarioView
from .views import PreLogoutUsuarioView, EditarUsuarioView

app_name='usuarios'

urlpatterns  = [
        path('registrar/',RegistrarUsuarioView.as_view(), name="registrar"),
        path('login/',LoginUsuarioView.as_view(), name="login"),
        path('prelogout/',login_required(PreLogoutUsuarioView.as_view()), name="prelogout"),
        path('logout/',login_required(LogoutUsuarioView.as_view()), name="logout"),
        path('editar/',EditarUsuarioView, name="editar"),
        
        path('password/change/', 
        auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), 
        name='password_change'),
        
        path('password_change/done/',
            auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
            name='password_change_done'),
        
        path('password/reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',
                        email_template_name = "password_reset_email.html",
                        success_url = reverse_lazy("usuarios:password_reset_done"),
                        subject_template_name = "password_reset_subject.txt"), 
                        name='password_reset'),
        
        path('password_reset/done/', 
                auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
                name='password_reset_done'),
        
        path('password/reset/<uidb64>/<token>/', 
                auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                            success_url = reverse_lazy("usuarios:password_reset_complete")), 
                name='password_reset_confirm'),
        
        path('password/reset/complete/', 
                auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
                name='password_reset_complete'),
        ]