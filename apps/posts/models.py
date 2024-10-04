from django.db import models
from django.utils import timezone

from apps.usuarios.models import Usuario


# CATEGORIA --------------------------------------
class Categoria(models.Model):
   nombre = models.CharField(max_length=30, null=False)

   def __str__(self):
      return self.nombre

# POSTEOS --------------------------------------
class Publicacion(models.Model):
   titulo_publicacion = models.CharField(max_length=50, null=False, help_text="Título de la publicación.")
   publicacion = models.TextField(max_length=250, null=False, help_text="Texto de la publicación.")
   imagen = models.ImageField(null=True, blank=True, default='static/img_default.png', upload_to='media')
   fecha_publicacion = models.DateTimeField(auto_now=True)
   fecha_modificacion = models.DateTimeField(default=timezone.now)
   usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null = True)
   categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin Categoría')

   class Meta:
      ordering = ('-titulo_publicacion',)

   def __str__(self):
      return self.titulo_publicacion
   
   def delete(self, using = None, keep_parents= False):
      self.imagen.delete(self.imagen.name)
      super().delete()


# COMENTARIOS --------------------------------------
class Comentarios(models.Model):
   comentario = models.TextField(max_length=150, null=False)
   editado= models.BooleanField(default=False)
   fecha_comentario = models.DateTimeField(auto_now=True)
   fecha_modificacion = models.DateTimeField(default=timezone.now)
   usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True)
   publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null = True)

   def __str__(self):
      return self.comentario
