from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class fotoUsuario(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
    
class usuario(models.Model):
    def url(self,nombreArchivo):
        ruta = "DatosMultimedia/Usuarios/%s%s" %(self.user.username,nombreArchivo)
        return ruta
    user = models.OneToOneField(User,related_name='usuario')
    foto = models.ImageField(upload_to='Usuario.fotoUsuario/bytes/filename/mimetype',null=True,blank=True)
    telefono = models.CharField(max_length=30)
    
def user_post_save(sender, instance, created, **kwargs):
        if created == True:
            usuari = usuario()
            usuari.user = instance
            usuari.save()
post_save.connect(user_post_save, sender=User)

def user_unicode_patch(self):
    return '%s %s' % (self.first_name, self.last_name)

User.__unicode__ = user_unicode_patch