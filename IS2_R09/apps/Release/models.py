from django.db import models
from IS2_R09.apps.Sprint.models import sprint
from IS2_R09.apps.Proyecto.models import proyecto

# Create your models here.
class release(models.Model):
    nombre = models.CharField(max_length=30)
    sprint_asociado= models.ForeignKey(sprint)
    proyecto_asociado = models.ForeignKey(proyecto,default=None)