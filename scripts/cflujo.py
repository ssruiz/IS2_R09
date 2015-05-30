# -*- encoding: utf-8 -*-
from IS2_R09.apps.Flujo.models import flujo,actividad

def run():
    """
        Scrip cflujo
        ============
        
        Script encargado de la creacion de flujos para el sistema.
    """
    print '--------------------------------------'
    print 'Creando Flujos...'
    a = actividad.objects.create(nombre='Análisis',order=0)
    a2 = actividad.objects.create(nombre='Diseño',order=1)
    a3 = actividad.objects.create(nombre='Implementación',order=2)
    
    a.save()
    a2.save()
    a3.save()
    
    
    f = flujo.objects.create(nombre='Flujo Cascada')
    f.actividades.add(a)
    f.actividades.add(a2)
    f.actividades.add(a3)
    
    f.save()
    
    #Flujo 2
    a = actividad.objects.create(nombre='Análisis',order=0)
    a2 = actividad.objects.create(nombre='Diseño',order=1)
    a3 = actividad.objects.create(nombre='Implementación',order=3)
    a4 = actividad.objects.create(nombre='Entrega',order=4)
    
    a.save()
    a2.save()
    a3.save()
    a4.save()
    f = flujo.objects.create(nombre='Flujo Entrega')
    f.actividades.add(a)
    f.actividades.add(a2)
    f.actividades.add(a3)
    f.actividades.add(a4)
    f.save()
    print 'Flujos Creados'
    print '--------------------------------------'