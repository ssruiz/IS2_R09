from IS2_R09.apps.Flujo.models import flujo,actividad

def run():
    """
        Scrip cflujo
        ============
        
        Script encargado de la creacion de flujos para el sistema.
    """
    a = actividad.objects.create(nombre='Analisis')
    a2 = actividad.objects.create(nombre='Disenho')
    a3 = actividad.objects.create(nombre='Implementacion')
    a4 = actividad.objects.create(nombre='Depuracion')
    a5 = actividad.objects.create(nombre='Mantenimiento')
    a.save()
    a2.save()
    a3.save()
    a4.save()
    a5.save()
    f = flujo.objects.create(nombre='Flujo Cascada')
    f.actividades.add(a)
    f.actividades.add(a2)
    f.actividades.add(a3)
    f.actividades.add(a4)
    f.actividades.add(a5)
    f.save()
    
    #Flujo 2
    a = actividad.objects.create(nombre='Analisis')
    a2 = actividad.objects.create(nombre='Disenho')
    a3 = actividad.objects.create(nombre='Implementacion')
    a4 = actividad.objects.create(nombre='Entrega')
    a5 = actividad.objects.create(nombre='Mantenimiento')
    a.save()
    a2.save()
    a3.save()
    a4.save()
    a5.save()
    f = flujo.objects.create(nombre='Flujo Entrega')
    f.actividades.add(a)
    f.actividades.add(a2)
    f.actividades.add(a3)
    f.actividades.add(a4)
    f.actividades.add(a5)
    f.save()
    