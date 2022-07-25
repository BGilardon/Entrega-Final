from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Posteo(models.Model):

    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50, null=True)
    autor = models.CharField(max_length=30, null=True)
    cuerpo = models.CharField(max_length=30)
    fecha = models.DateField()
    imagen = models.FileField(upload_to='media/', blank=True, null=True)

class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)


# Create your models here.

