'''from django.db import models
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
import datetime
# Create your models here.

class roles(models.Model):
    grupo = models.OneToOneField(Group,related_name='grupo')
    fecha = models.DateField()

def group_post_save(sender, instance, created, **kwargs):
        if created == True:
            rol = roles()
            rol.grupo = instance
            rol.fecha = datetime.datetime.now().date()
            rol.save()
post_save.connect(group_post_save, sender=Group)'''