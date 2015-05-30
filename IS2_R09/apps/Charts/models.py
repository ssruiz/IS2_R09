from django.db import models
from IS2_R09.apps.Sprint.models import sprint
from IS2_R09.apps.Proyecto.models import proyecto

# Create your models here.
class charts(models.Model):
    nombre = models.CharField(max_length=100,unique=False)
    ejey = models.PositiveIntegerField() # horas
    ejex = models.PositiveIntegerField() # dia que se realizo
    sprint_actual= models.ForeignKey(sprint,unique=False)
    proyect = models.ForeignKey(proyecto,default=None,unique=False)
    