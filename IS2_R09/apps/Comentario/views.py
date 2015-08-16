# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from IS2_R09.apps.US.models import us
from django.template.context import RequestContext
from IS2_R09.apps.Comentario.forms import comentario_form,\
    comentario_consulta_form
from IS2_R09.apps.Comentario.models import comentario
from django.http.response import HttpResponseRedirect, HttpResponse
import datetime
from IS2_R09.apps.Adjunto.forms import consultar_adjunto_form
from django.contrib.sites import requests
from django.views.decorators.csrf import csrf_exempt
from keyring.backend import json
from IS2_R09.apps.Flujo.models import kanban, flujo
from IS2_R09.apps.Sprint.models import sprint
from IS2_R09.apps.Proyecto.models import proyecto, Equipo
from IS2_R09.apps.Charts.models import charts
import datetime
# Create your views here.
def adm_comentario_view(request,id_us):
    """Vista que controla la interfaz de administracion de comentarios"""
    userst = us.objects.get(id=id_us)
    comentarios = userst.comentarios.all()
    ctx = {'comentarios':comentarios,'userid':id_us}
    return render_to_response('comentario/adm_comentario.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------

def crear_comentario_view(request,id_us):
    """Vista que controla creacion de comentarios"""
    form = comentario_form()
    if request.method == 'POST':
        ust= us.objects.get(id=id_us)
        form = comentario_form(request.POST)
        if form.is_valid():
            c = form.save()
            ust.comentarios.add(c)
            return HttpResponseRedirect('/adm_comentario/%s'%(id_us))
    form.fields['fecha_creacion'].initial =datetime.date.today()
    form.fields['fecha_ultima_mod'].initial =datetime.date.today()
    ctx = {'form':form,'userid':id_us}
    return render_to_response('comentario/crear_comentario.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------
def modificar_comentario_view(request, id_comentario,id_us):
    c = comentario.objects.get(id=id_comentario)
    print c
    form = comentario_form()
    if request.method == 'POST':
        form = comentario_form(request.POST, instance=c)
        if form.is_valid():
            # formulario validado correctamente
            
            
            form.save()
            c.fecha_ultima_mod = datetime.date.today()
            c.save()
            return HttpResponseRedirect('/adm_comentario/%s'%(id_us))
        
    if request.method == 'GET':
        print c
        form = comentario_form(instance=c)
        ctx = {'form': form,'userid':id_us}
        return render_to_response('comentario/modificar_comentario.html', ctx, context_instance=RequestContext(request))
    

#----------------------------------------------------------------------------------------------------------------
def eliminar_comentario_view(request, id_comentario,id_us):
    """Vista que controla la eliminacion de usuarios del sistema"""
    c = comentario.objects.get(id=id_comentario)
    userst = us.objects.get(id=id_us)
    if request.method == 'POST':
        c.delete()
        comentarios = userst.comentarios.all()
        ctx = {'comentarios':comentarios,'userid':id_us}
        return HttpResponseRedirect('/adm_comentario/%s'%(id_us),ctx)
    ctx = {'comentario': c,'userid':id_us}
    return render_to_response('comentario/eliminar_comentario.html', ctx, context_instance=RequestContext(request))


#----------------------------------------------------------------------------------------------------------------
def consultar_comentario_view(request, id_comentario,id_us):
    if request.method == 'GET':
        c= comentario.objects.get(id=id_comentario)
        form = comentario_consulta_form(instance=c)
        ctx = {'form': form,'userid':id_us}
        return render_to_response('comentario/consultar_comentario.html', ctx, context_instance=RequestContext(request))
    
@csrf_exempt
def crear_comentario_us(request):
    if request.is_ajax():
        
        
        ut= request.POST.get('k')
        k= kanban.objects.get(us=ut)
        nombr = request.POST.get('nombre')
        ht = request.POST.get('ht')
        
        
        ust = us.objects.get(id=ut)
        
        sp= sprint.objects.get(id=ust.sprint_asociado.id)
        estado= str(k.get_estado_display())
        pr = proyecto.objects.get(id=sp.proyect.id)
        
        if not us.objects.filter(id=ut,usuario_asignado=request.user).exists():
            if Equipo.objects.filter(proyect=pr,miembro=request.user).exists():
                e = Equipo.objects.get(proyect=pr,miembro=request.user)
                print e.rol.name
                print e.miembro
                if not e.rol.name == 'Scrum':
                    l = {'cambiar': 'no','mensaje':'No esta asignado al User Story y no posee permisos de Scrum master para agregar comentarios.'}
                    return HttpResponse(json.dumps(l))
            elif not request.user.is_staff:
                l = {'cambiar': 'no','mensaje':'No esta asignado al User Story y no posee permisos suficientes.'}
                return HttpResponse(json.dumps(l))
        
        coment = str(request.POST.get('c')) + ('\nFlujo: %s - Actividad: %s - Estado: %s \nRealizado por: %s' %(k.fluj,k.actividad,estado,request.user))
        c= comentario.objects.create(nombre=str(nombr),comentario=coment,fecha_creacion=datetime.date.today(),fecha_ultima_mod=datetime.date.today())
        # creando el burndownchart
        name = 'P:%s S:%s' %(pr.nombre,sp.nombre)
        
        ust.comentarios.add(c)
        ust.tiempo_trabajado+= int(ht)
        sp.tiempo_total+= int(ht)
        
        try:
            if pr.fecha_inicio:
                dias= (datetime.date.today() - pr.fecha_inicio).days + 1
            else:
                dias= 1
            print dias
            bd=charts.objects.get(sprint_actual=sp,proyect=sp.proyect,ejex=dias)
            bd.ejey -= int(ht)
            bd.save()
        except  Exception as e:
            if pr.fecha_inicio:    
                dias= (datetime.date.today() - pr.fecha_inicio).days + 1
            else:
                dias= 1
                pr.fecha_inicio= datetime.date.today()
                pr.save()
            try:
                horas_remanentes = sp.tiempo_estimado - int(ht)
                charts.objects.create(nombre=name,ejey=horas_remanentes,ejex=dias,sprint_actual=sp,proyect=sp.proyect)
            except  Exception as e:
                print 'aaa'
                print '%s (%s)' % (e.message, type(e))
            
            
        
            
        ht = sp.tiempo_total
        
        sp.save()
        ust.save()
        #Sprint culmina al llegar a las horas estimadas
        if sp.tiempo_total>=sp.tiempo_estimado:
            f = flujo.objects.get(id=k.fluj.id)
            uts = f.user_stories.all()
            for u in uts:
                ustaux = us.objects.get(id=u.id)
                ustaux.sprint_asociado = None
                ustaux.save()
            sp.finalizado='si'
            sp.fecha_fin= datetime.date.today()
            sp.save()
            p = proyecto.objects.get(id=ust.proyecto_asociado.id)
            p.sprint_actual= ''
            p.save()
        l = {'mensaje':'Comentario Creado','ht':ht}
        return HttpResponse(json.dumps(l))
