from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# USUARIOS --------------------------------------
class Usuario(AbstractUser):
   direccion = models.TextField(max_length=30)
      
   def __str__(self):
      return self.first_name+", "+self.last_name