from IS2_R09.apps.Proyecto.models import proyecto, Equipo
from IS2_R09.apps.Flujo.models import flujo
from django.contrib.auth.models import User,Group
import datetime

def run():
    f = flujo.objects.get(nombre='Flujo Cascada')
    f2 = flujo.objects.get(nombre='Flujo Entrega')
    r = Group.objects.get(name='Admin')
    r2 = Group.objects.get(name='Scrum')
    r3 = Group.objects.get(name='Developer')
    
    u = User.objects.get(username='Pablor')
    u2 = User.objects.get(username='Luzm')
    u3 = User.objects.get(username='Pedron')
    u4 = User.objects.get(username='Jes')
    u5 = User.objects.get(username='Joe')
    u6 = User.objects.get(username='Mari')
    # Proyecto 1
    p = proyecto.objects.create(nombre='Proyecto Supermarket',descripcion='Proyecto que contempla el control de stock de un supermercado',
                                fecha_creacion=datetime.date.today(),cliente=u3)
    p.flujos.add(f)
    p.save()
    equipo = Equipo.objects.create(proyect=p,miembro=u2,rol=r2)
    equipo2 = Equipo.objects.create(proyect=p,miembro=u,rol=r)
    equipo3 = Equipo.objects.create(proyect=p,miembro=u4,rol=r3)
    equipo.save()
    equipo2.save()
    equipo3.save()
    # Proyecto 2
    p2 = proyecto.objects.create(nombre='Proyecto Libreria',descripcion='Proyecto que contempla el control de las operaciones dentro de un libreria',
                                fecha_creacion=datetime.date.today(),cliente=u)
    p2.flujos.add(f2)
    p2.save()
    
    equipo = Equipo.objects.create(proyect=p2,miembro=u5,rol=r)
    equipo2 = Equipo.objects.create(proyect=p2,miembro=u6,rol=r3)
    equipo3 = Equipo.objects.create(proyect=p2,miembro=u2,rol=r2)
    equipo.save()
    equipo2.save()
    equipo3.save()
    
    #Proyecto 3
    p3 = proyecto.objects.create(nombre='Proyecto VideoClub',descripcion='Proyecto que contempla el control de las operaciones dentro de un videoclub',
                                fecha_creacion=datetime.date.today(),cliente=u6)
    p3.flujos.add(f)
    p3.flujos.add(f2)
    p3.save()
    equipo = Equipo.objects.create(proyect=p3,miembro=u3,rol=r2)
    equipo2 = Equipo.objects.create(proyect=p3,miembro=u2,rol=r)
    equipo3 = Equipo.objects.create(proyect=p3,miembro=u4,rol=r3)
    equipo4 = Equipo.objects.create(proyect=p3,miembro=u,rol=r3)
    equipo.save()
    equipo2.save()
    equipo3.save()
    equipo3.save()
    
    
    #Proyecto 4
    p4 = proyecto.objects.create(nombre='Proyecto Biblioteca',descripcion='Proyecto que contempla el control de las operaciones dentro de una biblioteca',
                                fecha_creacion=datetime.date.today(),cliente=u5)
    p4.flujos.add(f)
    p4.save()
    equipo = Equipo.objects.create(proyect=p4,miembro=u,rol=r2)
    equipo2 = Equipo.objects.create(proyect=p4,miembro=u2,rol=r)
    equipo3 = Equipo.objects.create(proyect=p4,miembro=u3,rol=r3)
    equipo4 = Equipo.objects.create(proyect=p4,miembro=u4,rol=r3)
    equipo5 = Equipo.objects.create(proyect=p4,miembro=u6,rol=r3)
    equipo.save()
    equipo2.save()
    equipo3.save()
    equipo4.save()
    equipo5.save()
    