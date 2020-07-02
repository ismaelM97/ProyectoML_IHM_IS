from django.db import models

# Create your models here.
#DJANgo da un efoque orietnado a objetos respecto a las BDD
#se crea una clase por cada tabla

class Medicos(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    cargo=models.CharField(max_length=30)
    email=models.EmailField()
    tfno=models.CharField(max_length=10)

