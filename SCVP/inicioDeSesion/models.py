from django.db import models

# Create your models here.
class Empleado(models.Model):
    numero_Empleado = models.CharField(max_length=8)
    contrasena_Empleado = models.CharField(max_length=20)