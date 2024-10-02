from django.contrib import admin

from .models import Categoria, Post


#-------------- POSTS
class PostAdmin(admin.ModelAdmin) :
   list_display = ('id',
                   'titulo', 
                   'post',
                   'fecha',
                   'imagen', 
                   'publicado',
                   'usuario',
                   'categoria')
   
   list_filter=('titulo','usuario')
   search_fields=('titulo','post')
   
admin.site.register(Categoria)
admin.site.register(Post,PostAdmin)


