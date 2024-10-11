from django.contrib import admin

from .models import Categoria, Publicacion, Comentario


#-------------- PUBLICACION
class CategoriaAdmin(admin.ModelAdmin) :
   list_display = ('id',
                   'categoria') 
   
   list_filter=('categoria',)
   
   search_fields=('categoria',)

admin.site.register(Categoria, CategoriaAdmin)


#-------------- PUBLICACION
class PublicacionAdmin(admin.ModelAdmin) :
   list_display = ('id',
                   'titulo_publicacion', 
                   'publicacion',
                   'imagen', 
                   'mostrar_imagen',
                   'fecha_publicacion',
                   'fecha_modificacion',
                   'usuario',
                   'categoria')
   
   list_filter=('titulo_publicacion','usuario')
   search_fields=('titulo_publicacion','publicacion')

admin.site.register(Publicacion,PublicacionAdmin)

#-------------- COMENTARIOS
class ComentarioAdmin(admin.ModelAdmin) :
   list_display = ('id',
                   'comentario', 
                   'editado',
                   'fecha_comentario', 
                   'fecha_modificacion',
                   'usuario',
                   'publicacion')
   
   list_filter=('comentario','usuario')
   search_fields=('comentario',)
   
admin.site.register(Comentario,ComentarioAdmin)



