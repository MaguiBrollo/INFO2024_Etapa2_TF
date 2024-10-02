from django.db import models

# Create your models here.


# USUARIOS --------------------------------------
class Usuario(models.Model):
   nombre = models.CharField(max_length=30, null=False)
   apellido = models.CharField(max_length=30, null=False)
   correo = models.EmailField(null=False)
   fechaNac = models.DateField(null=False, help_text = "Formato de Fecha <em>DD-MM-YYYY</em>.")
   foto = models.ImageField(null=True, blank=True, default='static/usuario.png', upload_to='media')
   
   """ class Meta:
      ordering = ('-apellido+nombre',) """

   def __str__(self):
      return self.apellido+", "+self.nombre
   
   def delete(self, using = None, keep_parents= False):
      self.foto.delete(self.foto.name)
      super().delete()