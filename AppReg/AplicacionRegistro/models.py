from django.db import models

# Create your models here.


class usuario(models.Model):
    nombre=models.ChardField(max_length=40)
    password=models.ChardField(max_length=40)
    email=models.EmailField()

class informacion(models.Model):
    titulo= models.ChardField(max_length=40)
    subtitulo= models.ChardField(max_length=40)
    info= models.ChardField(max_length=200)
