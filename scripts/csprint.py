<<<<<<< HEAD
# -*- encoding: utf-8 -*-
from IS2_R09.apps.Proyecto.models import proyecto
from IS2_R09.apps.Sprint.models import sprint

def run():
    print '--------------------------------------'
    print 'Creando Sprints'
    
    #Obteniendo los proyectos
    p = proyecto.objects.get(id=1)
    p2 = proyecto.objects.get(id=2)
    
    sp = sprint.objects.create(nombre='Sprint 1',descripcion='Sprint 1 proyecto 1',proyect=p)
    sp2 = sprint.objects.create(nombre='Sprint 2',descripcion='Sprint 2 proyecto 1',proyect=p)
    
    print 'Sprints creados'
    print '--------------------------------------'
    
    
=======
'''
@author: Melissa Bogado, Samuel Ruiz, Rafael Ricardo
'''
from IS2_R09.apps.Sprint.models import sprint
from IS2_R09.apps.Proyecto.models import proyecto

def run():
    """
        Script csprint
        ============
        
        Script encargado de la creacion de sprints para el sistema.
    """
    #Proyecto asociados a los sprints
    p1 = proyecto.objects.get(id=1)
    p2 = proyecto.objects.get(id=2)
    p3 = proyecto.objects.get(id=3)
    p4 = proyecto.objects.get(id=4)

    #Sprint 1
    s1 = sprint.objects.create(nombre='S1',descripcion='sprint 1',fecha_inicio='2015-05-10',fecha_fin='2015-05-30',tiempo_estimado=0,tiempo_total=300,proyect=p1)
    #Sprint 2
    s2 = sprint.objects.create(nombre='S2',descripcion='sprint 2',fecha_inicio='2015-05-05',fecha_fin='2015-05-30',tiempo_estimado=0,tiempo_total=250,proyect=p4)
    #Sprint 3
    s3 = sprint.objects.create(nombre='S3',descripcion='sprint 3',fecha_inicio='2015-05-12',fecha_fin='2015-05-30',tiempo_estimado=0,tiempo_total=400,proyect=p3)
    #Sprint 4
    s4 = sprint.objects.create(nombre='S4',descripcion='sprint 4',fecha_inicio='2015-05-19',fecha_fin='2015-05-30',tiempo_estimado=0,tiempo_total=230,proyect=p2)
    s1.save()
    s2.save()
    s3.save()
    s4.save()
>>>>>>> 031471800e70d02fa2704ff1c9b796e9dde3af57
