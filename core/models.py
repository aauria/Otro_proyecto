from django.db import models


# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=200,default='')
    apellido = models.CharField(max_length=200,default='')
    edad = models.IntegerField(default=0)
    email= models.EmailField(max_length=200,default='')
    sexo= models.CharField(max_length=1,default='')
    titulo_Profesion= models.CharField(max_length=15,default='')
    cedula=models.CharField(max_length=10,default='')
    curso_asignado=models.CharField(max_length=15,default='')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)