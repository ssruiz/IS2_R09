'''
Created on 30/4/2015

@author: meliam
'''
from django.db import models
"""Modelo de la clase Adjunto.
   Muestra los atributos relacionados a un Adjunto, los cuales son:
   nombre, descripcion, version, comentario_commit y archivo
"""
# Create your models here.

class adjunto(models.Model):
    def url(self,nombreArchivo):
        ruta = "DatosMultimedia/Archivos/%s%s" %(self.user.username,nombreArchivo)
        return ruta
    nombre = models.TextField(length=40) 
    descripcion = models.TextField(length=100)
    version = models.TextField(length=10)
    comentario_commit = models.TextField(length=100)
    archivo = models.FileField(upload_to=url)
