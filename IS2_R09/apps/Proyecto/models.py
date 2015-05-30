from django.db import models
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save
from IS2_R09.apps.Flujo.models import flujo
# Create your models here.

class proyecto(models.Model):
    miembro = models.ManyToManyField(User,through='Equipo',related_name='equipo',null=True,blank=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200)
    cliente = models.ForeignKey(User,related_name='cliente',null=True,blank=True,unique=False)
    fecha_creacion = models.DateField(blank=True)
    fecha_inicio = models.DateField(null=True,blank=True)
    fecha_fin = models.DateField(null=True,blank=True)
    estado = models.CharField(max_length=10,blank=True,default='Iniciado')
    flujos = models.ManyToManyField(flujo,null=True,blank=True)
    sprint_actual= models.CharField(max_length=30,null=True,blank=True,default='')
    def __str__(self):
        return self.nombre
    def estado_defatul(self):
        return {'estado':'iniciado'}

class Equipo(models.Model):
    proyect = models.ForeignKey(proyecto,related_name='proyecto')
    miembro = models.ForeignKey(User,related_name='usuario_proyec')
    rol = models.ForeignKey(Group,related_name='rol')    