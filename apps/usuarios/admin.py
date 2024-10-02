from django.contrib import admin
from .models import Usuario

# Register your models here.


#-------------- USUARIO
class UsuarioAdmin(admin.ModelAdmin):
   list_display = ('id',
                   'nombre', 
                   'apellido',
                   'correo',
                   'fechaNac', 
                   'foto')
   list_filter=('apellido','nombre')
   search_fields=('apellido','nombre')

admin.site.register(Usuario,UsuarioAdmin)
