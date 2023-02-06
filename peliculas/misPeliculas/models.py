from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    director = models.CharField(max_length=200, blank=True)
    fecha = models.DateField
    descripcion = models.CharField(max_length=300, null=True)

    def __str__(self) -> str:
        return self.titulo
