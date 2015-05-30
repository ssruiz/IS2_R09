# -*- encoding: utf-8 -*-
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
    print 'Creando User Stories...'
    #Proyecto asociados a los USs
    p1 = proyecto.objects.get(id=1)
    p2 = proyecto.objects.get(id=2)
    p3 = proyecto.objects.get(id=3)
    p4 = proyecto.objects.get(id=4)
    
    #user asociado a los USs
    
    #sprints asociado a los USs
    s1 = sprint.objects.get(id=1)
    s2 = sprint.objects.get(id=2)
    #US 1
    us1 = us.objects.create(nombre='us1',descripcion='User Story 1',prioridad=1,tiempo_estimado=30,proyecto_asociado=p1,sprint_asociado=s1)
    #US 2
    us2 = us.objects.create(nombre='us2',descripcion='User Story 2',prioridad=1,tiempo_estimado=25,proyecto_asociado=p1,sprint_asociado=s1)
    #US 3
    us3 = us.objects.create(nombre='us3',descripcion='User Story 3',prioridad=2,tiempo_estimado=15,proyecto_asociado=p1,sprint_asociado=s1)
    #US 4
    us4 = us.objects.create(nombre='us4',descripcion='User Story 4',prioridad=2,tiempo_estimado=10,proyecto_asociado=p1,sprint_asociado=s1)
    #US 5
    us5 = us.objects.create(nombre='us5',descripcion='User Story 5',prioridad=3,tiempo_estimado=5,proyecto_asociado=p1,sprint_asociado=s1)
    us6 = us.objects.create(nombre='us6',descripcion='User Story 6',prioridad=2,tiempo_estimado=18,proyecto_asociado=p1,sprint_asociado=s2)
    s1.tiempo_estimado+=85
    s2.tiempo_estimado+=18
    s1.save()
    s2.save()
    us1.save()
    us2.save()
    us3.save()
    us4.save()
    us5.save()
    us6.save()
    print 'User Story creados.'
