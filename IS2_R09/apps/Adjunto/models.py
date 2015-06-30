'''
Created on 30/4/2015

@author: meliam
'''
from django.db import models

# Create your models here.

class archivoUs(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class adjunto(models.Model):
    """Modelo de la clase Adjunto.
       Muestra los atributos relacionados a un Adjunto, los cuales son:
       nombre, descripcion, version, comentario_commit y archivo
    """
    def generate_filename(self, filename):
        url = "archivos/us/%s%s" % (self.nombre, filename)
        return url
    nombre = models.TextField(max_length=40) 
    descripcion = models.TextField(max_length=100)
    version = models.TextField(max_length=10)
    comentario_commit = models.TextField(max_length=100)
    archivo = models.FileField(upload_to='Adjunto.archivoUs/bytes/filename/mimetype',null=True,blank=True)
    def __unicode__(self):
        return self.nombre