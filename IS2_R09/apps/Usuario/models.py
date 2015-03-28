from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class usuario(models.Model):
    def url(self,nombreArchivo):
        ruta = "DatosMultimedia/Usuarios/%s%s" %(self.user.username,nombreArchivo)
        return ruta
    user = models.OneToOneField(User,related_name='usuario')
    foto = models.ImageField(upload_to=url)
    telefono = models.CharField(max_length=30)
    
def user_post_save(sender, instance, created, **kwargs):
        if created == True:
            usuari = usuario()
            usuari.user = instance
            usuari.save()
post_save.connect(user_post_save, sender=User)