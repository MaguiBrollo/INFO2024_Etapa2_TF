from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


from .models import Usuario

class RegitrarUsuarioForm(UserCreationForm):
   
   class Meta:
      model = Usuario 
      fields = [
            'first_name',
            'last_name',
            'email',
            'fecha_nacimiento',
            'foto', 
            'username', 
            'password1',
            'password2'
      ]
   def __init__(self, *args, **kwargs):
      super(RegitrarUsuarioForm, self).__init__(*args, **kwargs)

      self.fields['first_name'].widget.attrs['class'] = 'form-control'
      self.fields['first_name'].widget.attrs['placeholder'] = 'Nombres'

      self.fields['last_name'].widget.attrs['class'] = 'form-control'
      self.fields['last_name'].widget.attrs['placeholder'] = 'Apellidos'

      self.fields['email'].widget.attrs['class'] = 'form-control'
      self.fields['email'].widget.attrs['placeholder'] = 'Correo'

      self.fields['fecha_nacimiento'].widget.attrs['class'] = 'form-control'
      self.fields['fecha_nacimiento'].widget.attrs['placeholder'] = 'Fecha de nacimiento'

      self.fields['foto'].widget.attrs['class'] = 'form-control'
      self.fields['foto'].widget.attrs['placeholder'] = 'Foto de Perfil'

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['placeholder'] = 'Ingrese contraseña'
      self.fields['password2'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['placeholder'] = 'Vuelva a ingresar contraseña'



class LoginForm(forms.Form):
   username = forms.CharField(label= "Nombre de usuario:")
   password = forms.CharField(label = "Contraseña: ", widget=forms.PasswordInput)

   def login(self, request):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')
      user = authenticate(request, username=username, password = password)
      if user:
         login(request, user)