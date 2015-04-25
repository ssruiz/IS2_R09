# -*- encoding: utf-8 -*-

"""
    Modulo que especifíca el modelo a utilizar para los B{User Stories} de los clientes.  
    @author: Samuel Ruiz,Melissa Bogado,Rafael Ricardo
"""
__docformat__ = "Epytext" 
from django.db import models
from django.contrib.auth.models import User
#from IS2_R09.apps.Flujo.models import flujo
from IS2_R09.apps.Proyecto.models import proyecto
# Create your models here.
class us(models.Model):
    """
        @cvar nombre: Nombre que identifica al B{User Story}
        @type nombre: Varchar
        @cvar PRIORIDADES: Prioridades del B{User Story} (Alta,Media,Baja)
        @cvar descripcion: Breve descripción sobre el B{User Story}
        @type descripcion: Varchar
        @cvar tiempo_estimado: Estimación en horas que consumirá el desarrollo de un B{User Story}
        @type tiempo_estimado: Integer
        @cvar tiempo_trabajado: Horas que consumió el desarrollo de un B{User Story}
        @type tiempo_trabajado: Integer
        @cvar usuario_asignado: Lista de Usuarios asignados al desarrollo del B{User Story}
        @type usuario_asignado: User
        @cvar prioridad: Prioridad del B{User Story}
        @type prioridad: Varchar
        @cvar flujo_asignado: Flujo en el que se desarrolla el B{User Story}
        @type flujo_asignado: Foreign Key
        @cvar proyecto_asociado: Proyecto al que pertenece el B{User Story}
        @type proyecto_asociado: Foreign Key
        
    """
    PRIORIDADES = (
                   ('A', 'Alta'),
                   ('M', 'Media'),
                   ('B', 'Baja'),
                   )
                   
                   
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200)
    tiempo_estimado= models.IntegerField(null=True,blank=True)
    tiempo_trabajado= models.IntegerField(null=True,blank=True)
    usuario_asignado=models.ManyToManyField(User,null=True,blank=True)
    prioridad=models.CharField(max_length=1, choices=PRIORIDADES)
    #flujo_asignado=models.ForeignKey(flujo,null=True,blank=True,unique=False)
    proyecto_asociado=models.ForeignKey(proyecto,null=True,blank=True,unique=False)
    def __unicode__(self):
        """
            Método que permite mostrar los objectos de tipo B{User Story}
            por su nombre.
        """
        return self.nombre