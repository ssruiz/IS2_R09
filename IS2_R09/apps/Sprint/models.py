'''
Created on 23/4/2015

@author: meliam
'''
from django.db import models
"""Modelo de la clase Sprint.
   Muestra los atributos relacionados a un Sprint, los cuales son:
   fecha_creacion, datefield asignado por el sistema; fecha_inicio, datefield asignado por el usuario
   autorizado; fecha_fin datefield asignado por el sistema, release_asociado y flujo_asociado
"""
# Create your models here.

class sprint(models.Model):
#   nombre = models.TextField(length=40) 
    fecha_creacion = models.DateField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
#    release_asociado = models.ManyToManyField(Release,through='Release',related_name='release')
#    flujoasociado = models.ManyToManyField(flujo, related_name='flujo')
