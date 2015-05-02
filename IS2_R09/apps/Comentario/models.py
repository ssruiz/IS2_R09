from django.db import models

# Create your models here.
class comentario(models.Model):
    nombre = models.CharField(max_length=30)
    comentario = models.TextField(max_length=200)
    fecha_creacion = models.DateField(blank=True)
    fecha_ultima_mod = models.DateField(blank=True)
    def __str__(self):
        return self.nombre
    