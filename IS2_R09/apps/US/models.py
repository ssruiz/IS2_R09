from django.db import models
from django.contrib.auth.models import User
from IS2_R09.apps.Flujo.models import flujo
from IS2_R09.apps.Proyecto.models import proyecto
# Create your models here.
class us(models.Model):
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
    flujo_asignado=models.OneToOneField(flujo,null=True,blank=True)
    proyecto_asociado=models.OneToOneField(proyecto,null=True,blank=True)
    def __str__(self):
        return self.nombre