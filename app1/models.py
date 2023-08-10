from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
          return f"{self.nombre}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
          return f"{self.nombre}, {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    #esta clase meta sirve para definir como se vera en admin
    #en la clase meta se puede definir el orden, etc 
    class Meta:
         verbose_name = "Profesor"
         verbose_name_plural = "Profesores"
         ordering = ['nombre']


    def __str__(self):
          return f"{self.nombre}, {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField() 

    def __str__(self):
          return f"{self.fechaEntrega}"