from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
   nombre = models.CharField(max_length=30, null=False)

   def __str__(self):
      return self.nombre

class Post(models.Model):
   titulo = models.CharField(max_length=50, null=False, help_text="Texto de ayuda en el input")
   subtitulo = models.CharField(max_length=80, null=False)
   fecha = models.DateTimeField(auto_now=True)
   texto = models.CharField(max_length=50, null=False)
   categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin Categoría')
   imagen = models.ImageField(null=True, blank=True, default='static/img_default.png', upload_to='media')
   publicado = models.DateTimeField(default=timezone.now)

   class Meta:
      ordering = ('-publicado',)

   def __str__(self):
      return self.titulo
   
   def delete(self, using = None, keep_parents= False):
      self.imagen.delete(self.imagen.name)
      super().delete()
