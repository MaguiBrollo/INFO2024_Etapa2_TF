from django.contrib import messages
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage

from .forms import RegitrarUsuarioForm, LoginForm, EditarUsuarioForm
from .models import Usuario
# Create your views here.

#----------------------------------------
class RegistrarUsuarioView(CreateView):
   template_name = "registrar.html"
   form_class = RegitrarUsuarioForm
   model = Usuario
   success_url = reverse_lazy("usuarios:login")

   def form_valid(self, form):
      messages.success(self.request, 'Registro exitoso. Ahora puede Iniciar Sesión.')
      usuario=form.save()
      login(self.request, usuario) 
      return redirect('usuarios:login')

@login_required
def EditarUsuarioView(request):
   usuBuscado = request.user.id
   usuario = Usuario.objects.get(id = usuBuscado)
   viejaFoto = usuario.foto.name
   viejaFotoP = usuario.foto

   if request.method == 'POST':
      form = EditarUsuarioForm(request.POST, request.FILES,instance = usuario)
      if form.is_valid():
         usuario.first_name = form.cleaned_data['first_name']
         usuario.last_name = form.cleaned_data['last_name']
         usuario.email = form.cleaned_data['email']
         usuario.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
         usuario.foto = form.cleaned_data['foto']

      #si la nueva foto es distinta de la default   
      if usuario.foto.name != '../static/img_default/usu_default.png':
         img_default = '../static/img_default/usu_default.png'

         if viejaFoto != usuario.foto.name and viejaFoto != img_default:
            #eliminar img anterior, si es dist de la actual y dist de default
            default_storage.delete(viejaFotoP.path)

         usuario.save()
         return redirect('index')
   else:
      form = EditarUsuarioForm(instance = usuario)

   context = {
      'form': form,
   }
   return render(request, 'editarUsuario.html', context)


#----------------------------------------
class LoginUsuarioView(LoginView):
   template_name = "login.html"
   form_class = LoginForm
   model = Usuario
   redirect_authenticated_user =True
   
   def get_success_url(self):
      messages.success(self.request, 'Login exitoso.')
      return reverse('index')
   
#----------------------------------------
class PreLogoutUsuarioView(TemplateView):
   template_name ='preLogout.html'

#----------------------------------------  
class LogoutUsuarioView(LogoutView):
   template_name = "logout.html"
   model = Usuario
   def get_success_url(self):
      messages.success(self.request, 'Logout exitoso.')
      return reverse('usuarios:logout')
   