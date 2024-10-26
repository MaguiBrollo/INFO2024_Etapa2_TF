from django.db import models
from django.conf import settings
from apps.publicacion.models import Publicacion
from django.utils import timezone

def default_datatime():
    return timezone.now().isoformat()
class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios_comentario', on_delete=models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comentarios_autor_comentario', on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=default_datatime)
    fecha_modificacion = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f'{self.autor} comento en {self.publicacion} lo siguiente: {self.texto}'