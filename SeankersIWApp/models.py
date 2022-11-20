from django.db import models

# Create your models here.

class Sneaker(models.Model):
    nombre = models.CharField(max_length=30)
    talla = models.IntegerField()
    precio= models.IntegerField()

class Cliente(models.Model):
        nombre=models.CharField(max_length=50)
        password = models.CharField(max_length=50)

class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    
