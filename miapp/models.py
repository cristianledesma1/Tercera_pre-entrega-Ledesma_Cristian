from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Auto(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='autos')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.año})'

class Direccion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='direcciones')
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    localidad = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.calle}, {self.altura}, {self.localidad}'
