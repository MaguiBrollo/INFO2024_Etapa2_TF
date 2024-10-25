from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import format_html

from apps.usuarios.models import Usuario


# CATEGORIA --------------------------------------
class Categoria(models.Model):
   categoria = models.CharField(max_length=30, null=False, verbose_name="Categoria")

   def __str__(self):
      return self.categoria

# POSTEOS --------------------------------------
class Publicacion(models.Model):
   titulo_publicacion = models.CharField(max_length=50, null=False, verbose_name="Título", help_text="Título de la publicación.")
   publicacion = models.TextField(null=False, verbose_name="Texto",help_text="Texto de la publicación.")
   resumen = models.TextField(max_length=255, blank=True, null=True)
   imagen = models.ImageField(null=True, blank=True, 
                              default='../static/img_default/public_default.jpg', 
                              upload_to='publicaciones', 
                              verbose_name="Imagen")
   fecha_publicacion = models.DateTimeField(auto_now=True, verbose_name="Publicado")
   fecha_modificacion = models.DateTimeField(default=timezone.now , verbose_name="Modificado")
   usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null = True, verbose_name="Usuario")
   categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default=0, verbose_name="Categoría")

   class Meta:
      ordering = ('titulo_publicacion',)

   def __str__(self):
      return self.titulo_publicacion
   
   def mostrar_imagen(self):
      return format_html('<img src="{}" width="100" />', format(self.imagen.url))

   def delete(self, using = None, keep_parents= False):
      self.imagen.delete(self.imagen.name)
      super().delete()


# COMENTARIOS --------------------------------------
class Comentario(models.Model):
   """ comentario = models.TextField(max_length=150, null=False, verbose_name="Comentario")
   editado= models.BooleanField(default=False, verbose_name="Editado")
   fecha_comentario = models.DateTimeField(auto_now=True, verbose_name="Comentado el")
   fecha_modificacion = models.DateTimeField(default=timezone.now, verbose_name="Modificado")
   usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True, verbose_name="Usuario")
   publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null = True, verbose_name= "Publicación") """

   publicacion = models.ForeignKey(Publicacion, related_name='comentarios_publicacion', on_delete=models.CASCADE)
   autor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comentarios_autor_publicacion', on_delete=models.CASCADE)
   texto = models.TextField()
   fecha_creacion = models.DateTimeField(default=timezone.now)
   
   def __str__(self):
      return self.comentario
