from django.db import models

# Create your models here.

class Sneaker(models.Model):
    nombre = models.CharField(max_length=30)
    talla = models.IntegerField()

