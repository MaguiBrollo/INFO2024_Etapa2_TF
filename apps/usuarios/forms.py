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

class LoginForm(forms.Form):
   username = forms.CharField(label= "Nombre de usuario:")
   password = forms.CharField(label = "Contraseña: ", widget=forms.PasswordInput)

   def login(self, request):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')
      user = authenticate(request, username=username, password = password)
      if user:
         login(request, user)