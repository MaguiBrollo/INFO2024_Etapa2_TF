from django.contrib.auth.forms import UserCreationForm


from .models import Usuario

class RegitrarUsuarioForm(UserCreationForm):
   class Meta:
      model = Usuario 
      fields = (
            'first_name',
            'last_name',
            'email',
            'fecha_nacimiento',
            'foto', 
            'username', 
            'password1',
            'password2'
      )
