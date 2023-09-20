from django.db import models

# Create your models here.


class usuario(models.Model):
    nombre=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    email=models.EmailField()

class informacion(models.Model):
    titulo= models.CharField(max_length=40)
    subtitulo= models.CharField(max_length=40)
    info= models.CharField(max_length=200)
