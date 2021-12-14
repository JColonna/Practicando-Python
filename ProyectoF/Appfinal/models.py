from django.db import models

# Create your models here.


class Registro(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()

    def __str__(self):
        return f'Nombre {self.nombre}, Apellido: {self.apellido}, DNI Nº: {dni}'
