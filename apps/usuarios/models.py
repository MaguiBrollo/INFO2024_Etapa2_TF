from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.html import format_html


# USUARIOS --------------------------------------
class Usuario(AbstractUser):
   fecha_nacimiento = models.DateField(null=True, verbose_name="Fecha Nacimiento" )
   foto = models.ImageField(null=True, blank=True,
                     default='../static/img_default/usu_default.png', 
                     upload_to='usuarios', 
                     verbose_name="Foto de Perfil" )

     
   REQUIRED_FIELDS = [ 'first_name', 'last_name', 'email' ] #pide too para el super user
   USERNAME_FIELD = 'username'                                 

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
      return self.last_name +", "+ self.first_name
    
   def delete(self, using = None, keep_parents= False): #borrado en admin
      if self.foto.name != '../static/img_default/usu_default.png':
         self.foto.delete(self.foto.name)
      super().delete()

   def get_absolute_url(self):
      return reverse('index')

   def mostrar_foto(self):   #para el admin dj
      return format_html('<img src="{}" width="100" />', format(self.foto.url))

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