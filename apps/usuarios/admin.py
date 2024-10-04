from django.contrib import admin
from .models import Usuario

# Register your models here.


#-------------- USUARIO
class UsuarioAdmin(admin.ModelAdmin):
   list_display = ('last_name', 
                   'first_name',
                   'direccion')
   list_filter=('last_name', 
                   'first_name')
   search_fields=('last_name', 
                   'first_name')

admin.site.register(Usuario,UsuarioAdmin)
