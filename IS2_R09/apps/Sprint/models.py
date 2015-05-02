# -*- encoding: utf-8 -*-

"""
    Modulo que especifíca el modelo a utilizar para los B{Sprints} de los Proyectos.  
    @author: Samuel Ruiz,Melissa Bogado,Rafael Ricardo
"""
__docformat__ = "Epytext" 
from django.db import models
from django.contrib.auth.models import User
from IS2_R09.apps.Flujo.models import flujo
from IS2_R09.apps.Proyecto.models import proyecto
# Create your models here.
class sprint(models.Model):
    """
        @cvar nombre: Nombre que identifica al B{Sprint}
        @type nombre: Varchar
        @cvar descripcion: Breve descripción sobre el B{Sprint}
        @type descripcion: Varchar
        @cvar fecha_inicio: Fecha en que empieza a desarrollarse B{Sprint}, es especificado por el usuario
        en caso de ser el primer B{Sprint} del proyecto, en caso contrario tomará la fecha_fin del B{Sprint} actual
        si es seleccionado como B{Sprint} siguiente.
        @type fecha_inicio: Date
        @cvar fecha_fin: Última fecha en la que se desarrollará el B{Sprint}, este valor es calculado a partir
        de la especificación del usuario sobre la duración de cada B{Sprint} al crear un Proyecto.
        @type fecha_fin: Date 
        
    """
                   
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=100)
    fecha_inicio= models.DateField(null=True,blank=True)
    fecha_fin= models.DateField(null=True,blank=True)
    proyect = models.ForeignKey(proyecto,null=True,blank=True)
    #fechacreacion?
    #usuario_asignado=models.ManyToManyField(User,null=True,blank=True)
    #prioridad=models.CharField(max_length=1, choices=PRIORIDADES)
    #flujo_asignado=models.ForeignKey(flujo,null=True,blank=True,unique=False)
    #proyecto_asociado=models.ForeignKey(proyecto,null=True,blank=True,unique=False)
    def __str__(self):
        """
            Método que permite mostrar los objectos de tipo B{Sprint}
            por su nombre.
        """
        return self.nombre
