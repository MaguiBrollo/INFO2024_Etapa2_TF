from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from .models import Usuario

#-----------------------------------------------------
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

#-----------------------------------------------------
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
      self.request = kwargs.pop('request', None)
      super(LoginForm,self).__init__(*args,**kwargs)
      self.fields["username"].widget.attrs.update({'class' : 'form-control','placeholder' : "Nombre de usuario", 'type' : 'text'})
      self.fields["password"].widget.attrs.update({'class' : 'form-control','placeholder' : "Contraseña", 'type' : 'text'})

#-----------------------------------------------------
class EditarUsuarioForm(forms.ModelForm):
   
   class Meta:
      model = Usuario 
      fields = [
            'first_name',
            'last_name',
            'email',
            'fecha_nacimiento',
            'foto' 
      ]
      exclude = ['username','password']

   def __init__(self, *args, **kwargs):
      super(EditarUsuarioForm, self).__init__(*args, **kwargs)

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
