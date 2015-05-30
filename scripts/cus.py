'''
@author: Melissa Bogado, Samuel Ruiz, Rafael Ricardo
'''
from IS2_R09.apps.US.models import us
from IS2_R09.apps.Sprint.models import sprint
from IS2_R09.apps.Proyecto.models import proyecto
from django.contrib.auth.models import User

def run():
    """
        Script cUS
        ============
        
        Script encargado de la creacion de US para el sistema.
    """
    #Proyecto asociados a los USs
    p1 = proyecto.objects.get(id=1)
    p2 = proyecto.objects.get(id=2)
    p3 = proyecto.objects.get(id=3)
    p4 = proyecto.objects.get(id=4)
    
    #user asociado a los USs
    u1 = User.objects.get(id=1)
    u2 = User.objects.get(id=2)
    u3 = User.objects.get(id=3)
    u4 = User.objects.get(id=4)
    u5 = User.objects.get(id=5)
    
    #sprints asociado a los USs
    s1 = sprint.objects.get(id=1)
    s2 = sprint.objects.get(id=2)
    s3 = sprint.objects.get(id=3)
    s4 = sprint.objects.get(id=4)
    #US 1
    us1 = us.objects.create(nombre='us1',descripcion='User Story 1',proyecto_asociado=p2,sprint_asociado=s3)
    #US 2
    us2 = us.objects.create(nombre='us2',descripcion='User Story 2',proyecto_asociado=p1,sprint_asociado=s2)
    #US 3
    us3 = us.objects.create(nombre='us3',descripcion='User Story 3',proyecto_asociado=p1,sprint_asociado=s1)
    #US 4
    us4 = us.objects.create(nombre='us4',descripcion='User Story 4',proyecto_asociado=p3,sprint_asociado=s4)
    #US 5
    us5 = us.objects.create(nombre='us5',descripcion='User Story 5',proyecto_asociado=p4,sprint_asociado=s2)
    
    us1.save()
    us2.save()
    us3.save()
    us4.save()
    us5.save()
