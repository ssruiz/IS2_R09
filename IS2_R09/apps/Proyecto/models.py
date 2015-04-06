from django.db import models
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save
# Create your models here.

class proyecto(models.Model):
    miembro = models.ManyToManyField(User,through='Equipo',related_name='equipo',null=True,blank=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200)
    cliente = models.OneToOneField(User,related_name='cliente',null=True,blank=True)
    fecha_creacion = models.DateField(blank=True)
    fecha_inicio = models.DateField(blank=True)
    fecha_fin = models.DateField(blank=True)
    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    proyect = models.ForeignKey(proyecto,related_name='proyecto')
    miembro = models.ForeignKey(User,related_name='usuario_proyec')
    rol = models.ForeignKey(Group,related_name='rol')