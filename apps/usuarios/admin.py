from django.contrib import admin
from .models import Usuario

# Register your models here.


#-------------- USUARIO
class UsuarioAdmin(admin.ModelAdmin):
   list_display = ('id','nombre_usuario', 
                   'apellidos',
                   'nombres',
                   'correo',
                   'fecha_nacimiento',
                   'foto',
                   'mostrar_foto',
                  'is_staff',
                  'is_active',
                  'is_superuser',
                  'last_login',
                  'date_joined' )
   
   fields = ('username', 
            'password',
            'first_name',
            'last_name',
            'email',
            'fecha_nacimiento',
            'foto', 
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined' )

   list_filter = ('first_name','last_name')

   search_fields=('apellidos','nombres', 'nombre_usuario')

admin.site.register(Usuario,UsuarioAdmin)

""" 
username
first_name
last_name
email
password
groups
user_permissions
is_staff
is_active
is_superuser
last_login
date_joined 
"""