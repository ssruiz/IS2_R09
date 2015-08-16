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
