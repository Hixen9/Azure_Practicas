from django.db import models

# Create your models here.

class Imagenes(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="productos/", null=True,blank=True)