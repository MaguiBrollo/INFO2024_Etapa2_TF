from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

@admin.register(Post)   #el decorador admin.register para ahorrarte admin.site.register(Post).
class AplicacionAdmin(admin.ModelAdmin) :
   list_display = ('id','titulo', 'subtitulo','fecha','texto','categoria','imagen', 'publicado')
   list_filter=('titulo','fecha')
   search_fields=('autor','texto')

   admin.site.register(Categoria) #aunque se use decorador falta register de categoria.
