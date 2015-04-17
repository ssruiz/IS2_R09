# -*- encoding: utf-8 -*-
from django.db import models
# Create your models here.

#----------------------------------------------------------------------------------------------
class actividad(models.Model):
    nombre = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.nombre
#----------------------------------------------------------------------------------------------
class flujo(models.Model):
    nombre = models.CharField(max_length=30)
    actividades = models.ManyToManyField(actividad)
    def __str__(self):
        return self.nombre

'''
ESTADOS = (
               ('td','to do'),
               ('dg', 'doing'),
               ('de', 'done'),
               )
    nombre = models.CharField(max_length=30)
    estado = models.CharField(max_length=2,choices=ESTADOS)
    '''