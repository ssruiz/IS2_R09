"""
Created on 15/5/2015
  Modulo que especifíca el modelo a utilizar para los B{Releases} de los Proyectos.  
    @author: Samuel Ruiz,Melissa Bogado,Rafael Ricardo
"""
__docformat__ = "Epytext"
from django.db import models
#from django.db.models.signals import post_save
from IS2_R09.apps.Sprint.models import sprint
from IS2_R09.apps.US.models import us
# Create your models here.

"""
        @cvar version: Nombre que identifica al B{Release}
        @type version: Varchar
        @cvar fecha_creacion: Fecha de lanzamiento del B{Release}
        @type fecha_creacion: Date
        @cvar sprints_asociados: Lista de Sprints asociados al B{Release}
        @type sprints_asociados: Sprint
        @cvar us_asociados: Lista de User Stories asociados al B{Release}
        @type us_asociados: us 
"""
class release(models.Model):
    version = models.CharField(max_length=30)
    fecha_creacion = models.DateField(blank=True)
    sprints_asociados = models.ManyToManyField(sprint,null=True,blank=True)
    us_asociados = models.ManyToManyField(us,null=True,blank=True)
    def __str__(self):
        """
            Método que permite mostrar los objectos de tipo B{Release}
            por su codigo de version.
        """
        return self.version