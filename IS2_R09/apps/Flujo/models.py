# -*- encoding: utf-8 -*-
"""
    Modelos
    =======
    
    Módulo que define la estructura de un L{Flujo<IS2_R09.apps.Flujo>} y como se guardará en la
    base de datos.
"""
from django.db import models
# Create your models here.

#----------------------------------------------------------------------------------------------
class actividad(models.Model):
    """
        Modelo de Actividad
        ===================
        Clase que define una actividad de un L{Flujo<IS2_R09.apps.Flujo>}.
        @cvar nombre: Nombre de la actividad.
        @type nombre: Varchar
    """
    nombre = models.CharField(max_length=30,unique=False)
    def __unicode__(self):
        """
            Método que permite representar los objectos de la clase L{Actividad<IS2_R09.apps.Flujo.models.actividad>}
            mediante su nombre.
            @return: Varchar
        """
        return self.nombre
#----------------------------------------------------------------------------------------------
class flujo(models.Model):
    """
        Model de Flujo
        ==============
        
        Clase que define un B{Flujo}
        @cvar nombre: Nombre asignado al Flujo.
        @type nombre: Varchar
        @cvar actividades: Lista de actividades que tiene el B{Flujo}, mediante la relación 
        ManytoMan(Muchos a muchos) con L{Actividad<IS2_R09.apps.Flujo.models.actividad>}
        @type actividades: L{Actividad<IS2_R09.apps.Flujo.models.actividad>}
    """
    nombre = models.CharField(max_length=30)
    actividades = models.ManyToManyField(actividad)
    user_stories = models.ManyToManyField('US.us',through='kanban',related_name='userstories',null=True,blank=True)
    def __unicode__(self):
        """
            Método que permite representar los objectos de la clase L{Flujo<IS2_R09.apps.Flujo.models.actividad>}
            mediante su nombre.
            @return: Varchar
        """
        return self.nombre
 
class kanban(models.Model):
    """
        Modelo de Kanban
        ================
        
    """
    ESTADOS = (
               ('td','to do'),
               ('dg', 'doing'),
               ('de', 'done'),
               )
    fluj = models.ForeignKey(flujo,related_name='flujo',null=True,blank=True)
    actividad = models.ForeignKey(actividad,related_name='actividad',null=True,blank=True)
    us = models.ForeignKey('US.us',related_name='user_story',null=True,blank=True)
    estado = models.CharField(max_length=2,choices=ESTADOS,default='td',null=True,blank=True)

    
'''
ESTADOS = (
               ('td','to do'),
               ('dg', 'doing'),
               ('de', 'done'),
               )
    nombre = models.CharField(max_length=30)
    estado = models.CharField(max_length=2,choices=ESTADOS)
    '''