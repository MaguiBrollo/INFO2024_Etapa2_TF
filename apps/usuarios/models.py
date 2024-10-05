from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# USUARIOS --------------------------------------
class Usuario(AbstractUser):
   fecha_nacimiento = models.DateField(null=True, verbose_name="Fecha Nacimiento")
   foto = models.ImageField(null=True, blank=True, default='static/usuario.png', upload_to='media', verbose_name="Foto de Perfil")
      
   @property
   def apellidos(self):
      return self.last_name
   
   @property
   def nombres(self):
      return self.first_name
   
   @property
   def nombre_usuario(self):
      return self.username
   
   @property
   def correo(self):
      return self.email
   
   @property
   def contrasenia(self):
      return self.password

   def __str__(self):
      return self.first_name+", "+self.last_name
   
   def __str__(self):
      return self.apellidos+", "+self.nombres
   
   def delete(self, using = None, keep_parents= False):
      self.foto.delete(self.foto.name)
      super().delete()


""" 
username
first_name
last_name
email
password
groups
user_permissions
is_staff
is_active
is_superuser
last_login
date_joined 
"""