from django.contrib import admin
from .models import Usuario

# Register your models here.


#-------------- USUARIO
class UsuarioAdmin(admin.ModelAdmin):
   list_display = ('nombre_usuario', 
                   'apellidos',
                   'nombres',
                   'correo',
                   'fecha_ncimiento',
                   'foto')
   list_filter=('apellidos','nombres')
   search_fields=('apellidos','nombres', 'nombre_usuario')

admin.site.register(Usuario,UsuarioAdmin)
