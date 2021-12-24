from django.db import models
from django.db.models.base import Model

# Create your models here.


class FormularioVentas(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return (f'Nombre: {self.nombre}, Telefono: {self.telefono}')

class FormularioCursos(models.Model):
    curso = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return (f'Nombre: {self.nombre}, Telefono: {self.telefono}')        


