from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sneaker(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300, default="")
    talla = models.IntegerField()
    precio= models.IntegerField(default=0)

    def __str__(self):
        return "Nombre: "+self.nombre
        

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Compra(models.Model):
    id_Sneaker = models.CharField(max_length=50, default="0")
    id_Cliente = models.CharField(max_length=50, default="0")
    precio = models.IntegerField(default=0)
    
