from django.db import models

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField
    email= models.EmailField
    sexo= models.CharField(max_length=1)
    user= models.CharField(max_length=15)
    user_mod=models.CharField(max_length=15)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)