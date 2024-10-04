from django.contrib import admin

from .models import Categoria, Publicacion


#-------------- POSTS
class PublicacionAdmin(admin.ModelAdmin) :
   list_display = ('id',
                   'titulo_publicacion', 
                   'publicacion',
                   'imagen', 
                   'fecha_publicacion',
                   'fecha_modificacion',
                   'publicado',
                   'usuario',
                   'categoria')
   
   list_filter=('titulo_publicacion','usuario')
   search_fields=('titulo_publicacion','publicacion')
   
admin.site.register(Categoria)
admin.site.register(Publicacion,PublicacionAdmin)


