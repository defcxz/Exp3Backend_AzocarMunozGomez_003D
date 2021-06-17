from django.db import models

# Create your models here.

class Mensaje(models.Model):
   nomApellido = models.CharField(max_length=50, verbose_name="Nombre y Apellido")
   email       = models.CharField(max_length=50, verbose_name="Email")
   telefono    = models.CharField(max_length=12, verbose_name="Telefono")
   asunto      = models.CharField(max_length=50, verbose_name="Asunto")
   mensaje     = models.CharField(max_length=500, verbose_name="Mensaje")

   def __str__(self):
      return self.nomApellido