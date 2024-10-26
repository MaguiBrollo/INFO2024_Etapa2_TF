from django.contrib import admin
from apps.comentario.models import Comentario

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id','publicacion', 'autor', 'texto')
    list_filter = ('publicacion', 'autor')

admin.site.register(Comentario, ComentarioAdmin)