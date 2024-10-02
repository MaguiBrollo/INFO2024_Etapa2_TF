from django.db import models
from django.utils import timezone

from apps.usuarios.models import Usuario


# CATEGORIA --------------------------------------
class Categoria(models.Model):
   nombre = models.CharField(max_length=30, null=False)

   def __str__(self):
      return self.nombre

# POSTEOS --------------------------------------
class Post(models.Model):
   titulo = models.CharField(max_length=50, null=False, help_text="Título del post")
   post = models.TextField(max_length=250, null=False, help_text="Texto del post")
   fecha = models.DateTimeField(auto_now=True)
   imagen = models.ImageField(null=True, blank=True, default='static/img_default.png', upload_to='media')
   publicado = models.DateTimeField(default=timezone.now)
   usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True)
   categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin Categoría')

   class Meta:
      ordering = ('-publicado',)

   def __str__(self):
      return self.titulo
   
   def delete(self, using = None, keep_parents= False):
      self.imagen.delete(self.imagen.name)
      super().delete()
