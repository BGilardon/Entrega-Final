from django.db import models
from django.contrib.auth.models import User

# modelo del avatar

class Posteo(models.Model):

    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=200) 
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='media', blank=True, null=True)

class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)


# Create your models here.

class Curso(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    comision = models.IntegerField()



class Profesor(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional

    profesion = models.CharField(max_length=30)

    # dni = models.IntegerField()

    class Meta:
        verbose_name_plural = "Profesores"

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self) -> str: # modificar como se visualiza
        return f"Entregable: {self.nombre} en la fecha {self.fechaEntrega}"