#!/usr/bin/python
# -*- encoding: utf-8 -*-
from IS2_R09.apps.Proyecto.forms import proyecto_form, equipo_form,cantidad_form,modificar_form,consultar_form,buscar_proyecto_form
from django.shortcuts import render_to_response
from IS2_R09.apps.Proyecto.models import proyecto,Equipo
from django.template.context import RequestContext
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
import datetime
from django.http.response import HttpResponseRedirect, HttpResponse
from IS2_R09.apps.US.models import us
from IS2_R09.apps.Flujo.models import kanban, flujo, actividad
from IS2_R09.apps.Notificaciones.views import notificar_asignacion_proyecto,\
    notificar_mod_proyecto, notificar_eli_proyecto
from keyring.backend import json
from IS2_R09.apps.Sprint.models import sprint
from django.core.context_processors import media, csrf
from chartit import DataPool,Chart
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url= URL_LOGIN)
def adm_proyecto_view(request):
    ''''Vista que controla la interfaz de administracion de proyectos'''
    proyectos= proyecto()
    if request.user.is_staff:
        '''Si el usuario es administrador se le listan todos los proyectos'''
        proyectos = proyecto.objects.all()
        ctx={'proyectos':proyectos,'form':buscar_proyecto_form()}
        return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
    ''''En caso contrario se le lista solo los proyectos al que esta asignado'''
    proyectos = proyecto.objects.filter(miembro=request.user)
    ctx={'proyectos':proyectos,'form':buscar_proyecto_form()}
    return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def crear_proyecto_view(request):
    '''Vista que controla creacion de Proyectos'''
    form= proyecto_form()
    if request.method == 'POST':
        form = proyecto_form(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                proyectos = proyecto.objects.all()
                ctx={'proyectos':proyectos,'mensaje':'Proyecto creado','form':buscar_proyecto_form()}
                return HttpResponseRedirect('/adm_proyecto/',ctx)
            else:
                proyectos = proyecto.objects.filter(miembro=request.user)
                ctx={'proyectos':proyectos,'mensaje':'Proyecto creado','form':buscar_proyecto_form()}
                return HttpResponseRedirect('/adm_proyecto/',ctx)
    form.fields['fecha_creacion'].initial = datetime.date.today()        
    ctx = {'form':form}
    return render_to_response('proyecto/crear_proyecto.html',ctx,context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def asignar_equipo_view(request,id_proyecto):
    '''Vista que controla la asignacion de usuario al equipo de un proyecto'''
    p = proyecto.objects.get(pk=id_proyecto)
    c= cantidad_form()
    equipo_formset = modelformset_factory(Equipo, form=equipo_form)
    if request.method == 'POST':
        formset= equipo_formset(request.POST)
        if formset.is_valid():
            formset.save()
            notificar_asignacion_proyecto(p.miembro.all(),p)
            if request.user.is_staff:
                proyectos = proyecto.objects.all()
                ctx={'proyectos':proyectos,'mensaje':'Equipo Modificado','form':buscar_proyecto_form()}
                return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
            else:
                proyectos = proyecto.objects.filter(miembro=request.user)
                ctx={'proyectos':proyectos,'mensaje':'Equipo Modificado','form':buscar_proyecto_form()}
                return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
    
    ctx = {'aux':c,'p':p.id}
    return render_to_response('proyecto/asignar_equipo.html',ctx,context_instance=RequestContext(request))
#------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def cantidad_equipo_view(request,id_proyecto):
    '''Esta vista esta pensada para poder agregar mas de un usuario a un equipo de un proyecto
        Simplemente adapta la pagina de creacion mediante el modelformset de Django, permitiendo
        incluir mas de un formulario(basado en el modelo Equipo) y asi poder generar o asignar mas de
        un usuario al equipo del proyecto
    '''
    c= cantidad_form()
    equipo_formset = modelformset_factory(Equipo,form=equipo_form)
    formset= equipo_formset()
    if request.method == 'POST':
        p = proyecto.objects.get(pk=id_proyecto)
        c= cantidad_form(request.POST)
        if c.is_valid():
            cantidad= c.cleaned_data['cantidad']
            equipo_formset = modelformset_factory(Equipo,form=equipo_form,extra=int(cantidad))
            formset= equipo_formset(queryset=Equipo.objects.none())
            for f in formset:
                f.fields['proyect'].initial= p
                f.fields['miembro'].queryset= User.objects.exclude(id__in=p.miembro.all())
            ctx = {'form':formset,'p':p.id}
            return render_to_response('proyecto/asignar_equipo.html',ctx,context_instance=RequestContext(request))
        
    ctx = {'aux':c,'p':p.id}
    return render_to_response('proyecto/asignar_equipo.html',ctx,context_instance=RequestContext(request))

@login_required(login_url= URL_LOGIN)
def modificar_proyecto_view(request,id_proyecto):
    if request.method == 'POST':
        proyect = proyecto.objects.get(id=id_proyecto)
        form = modificar_form(request.POST,instance=proyect)
        if form.is_valid():
            form.save()
            notificar_mod_proyecto(proyect.miembro.all(),proyect)
            if request.user.is_staff:
                proyectos = proyecto.objects.all()
                ctx={'proyectos':proyectos,'mensaje':'Proyecto modificado','form':buscar_proyecto_form()}
                return HttpResponseRedirect('/adm_proyecto/',ctx)
            else:
                proyectos = proyecto.objects.filter(miembro=request.user)
                ctx={'proyectos':proyectos,'mensaje':'Proyecto Modificado','form':buscar_proyecto_form()}
                return HttpResponseRedirect('/adm_proyecto/',ctx)
    
    if request.method=='GET':
        proyect = proyecto.objects.get(id=id_proyecto)
        form = modificar_form(instance= proyect)
        ctx = {'form':form,'cliente':proyect.cliente}
        return render_to_response('proyecto/modificar_proyecto.html',ctx,context_instance=RequestContext(request))
#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def eliminar_proyecto_view(request,id_proyecto):
    '''vista que controla la eliminacion de usuarios del sistema'''
    proyect = proyecto.objects.get(pk=id_proyecto)
    if request.method == 'POST':
        p = proyect.nombre
        e= proyect.miembro.all()
        notificar_eli_proyecto(e,p)
        proyect.delete()
        if request.user.is_staff:
                proyectos = proyecto.objects.all()
                ctx={'proyectos':proyectos,'mensaje':'Proyecto Eliminado','form':buscar_proyecto_form()}
                return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
        else:
            proyectos = proyecto.objects.filter(miembro=request.user)
            ctx={'proyectos':proyectos,'mensaje':'Proyecto Eliminado','form':buscar_proyecto_form()}
            return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
    
    ctx = {'proyecto': proyect}
    return render_to_response('proyecto/eliminar_proyecto.html', ctx, context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def consultar_proyecto_view(request,id_proyecto):
    if request.method=='GET':
        proyect = proyecto.objects.get(id=id_proyecto)
        roles = Equipo.objects.filter(proyect=proyect)
        
        equipo = proyect.miembro.all()
        form = consultar_form(instance= proyect)
        form.fields['miembro'].queryset=proyect.miembro.all()
        form.fields['flujos'].queryset=proyect.flujos.all()
        flujos = proyect.flujos.all()
        sprints = sprint.objects.filter(proyect=proyect,finalizado='no')
        client = proyect.cliente
        list= zip(equipo,roles)
        ust = us.objects.filter(proyecto_asociado=id_proyecto,release_asociado=None).order_by('prioridad')
        
        ctx = {'form':form,'list':list,'ust':ust,'cliente':client,'flujos':flujos,'sprints':sprints}
        return render_to_response('proyecto/consultar_proyecto.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def buscar_proyecto_view(request):
    form = buscar_proyecto_form()
    if(request.method=='POST'):
        form = buscar_proyecto_form(request.POST)
        form2 = buscar_proyecto_form()
        if form.is_valid():
            busqueda= form.cleaned_data['opciones']
            parametro = form.cleaned_data['busqueda']
            if busqueda== 'nombre':
                p = proyecto.objects.filter(nombre=parametro)
                ctx = {'mensaje': 'Proyecto con nombre %s' %(parametro),'proyectos':p,'form':form2}
                return render_to_response('proyecto/adm_proyecto.html', ctx, context_instance=RequestContext(request))
            elif busqueda== 'cliente':
                try:
                    u = User.objects.get(username=parametro)
                    p = proyecto.objects.filter(cliente=u)
                    ctx = {'mensaje': 'Proyecto con cliente %s' %(u),'proyectos':p,'form':form2}
                    return render_to_response('proyecto/adm_proyecto.html', ctx, context_instance=RequestContext(request))
                except:
                        if request.user.is_staff:
                            proyectos = proyecto.objects.all()
                            ctx={'proyectos':proyectos,'mensaje':'Cliente con username %s no existe'%(parametro),'form':buscar_proyecto_form()}
                            return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
                        else:
                            proyectos = proyecto.objects.filter(miembro=request.user)
                            ctx={'proyectos':proyectos,'mensaje':'Cliente con username %s no existe'%(parametro),'form':buscar_proyecto_form()}
                            return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
                    
    ctx = {'form': form}
    return render_to_response('proyecto/adm_proyecto.html', ctx, context_instance=RequestContext(request))

@login_required(login_url= URL_LOGIN)
def kanban_proyecto_view(request,id_proyecto):
    proyect = proyecto.objects.get(id=id_proyecto)
    #fj = proyect.flujos.first()
    #ust= fj.user_stories.all()
    #k = kanban.objects.first()
    #g = kanban.objects.filter(us__in=ust).order_by('actividad')
    #kan = kanban_form(instance=k)
    if request.method == 'GET':
        #kanban_formset = modelformset_factory(kanban,form=kanban_form,extra=0)
        #print kanban.objects.filter(us__in=ust).count()
        #formset= kanban_formset(queryset=kanban.objects.filter(us__in=ust).order_by('actividad'))    
        #form = proyecto_kanban_form(instance=proyect)
        #form.fields['flujos'].queryset = proyect.flujos.all()
        fji = proyect.flujos.all()
        ctx = {'form':fji,'p':proyect}
        return render_to_response('proyecto/kanban_proyecto.html', ctx, context_instance=RequestContext(request))
    
@login_required(login_url= URL_LOGIN)
def ustload(request):
    if request.is_ajax():
        idf= request.GET['fluj_id']
        p = request.GET['p']
        fj= flujo.objects.get(id=idf)
        acti = fj.actividades.all()
        pr = proyecto.objects.get(id=p)
        f= pr.flujos.get(id=idf)
        ult = fj.actividades.all().order_by('-order')[0]
        if pr.sprint_actual == '':
            ust = us.objects.filter(proyecto_asociado=pr,sprint_asociado__finalizado='no').order_by('prioridad')
            
            releases = kanban.objects.filter(us__in=ust,fluj=fj,actividad=ult,estado='de').order_by('prioridad')
            k= kanban.objects.filter(us__in=ust,fluj=fj).order_by('prioridad')
            print f
            baja = f.user_stories.filter(prioridad=3).exclude(id__in=releases).count()
            media = f.user_stories.filter(prioridad=2).exclude(id__in=releases).count()
            alta = f.user_stories.filter(prioridad=1).exclude(id__in=releases).count()
            return render_to_response('proyecto/kanban_proyecto.html',{
                    'fs': k,'baja':baja,'media':media,'alta':alta,'releases':releases,'actividades':acti,'sp':'Ninguno en desarrollo','flujo':f},context_instance=RequestContext(request))
        else:
            sp= sprint.objects.get(id=pr.sprint_actual)
            ust = f.user_stories.filter(sprint_asociado=sp,sprint_asociado__finalizado='no').order_by('prioridad')
            
            releases = kanban.objects.filter(us__in=ust,fluj=fj,actividad=ult,estado='de').order_by('prioridad')
            k= kanban.objects.filter(us__in=ust,fluj=fj).order_by('prioridad')
            baja = f.user_stories.filter(sprint_asociado=sp,prioridad=3).exclude(id__in=releases).count()
            media = f.user_stories.filter(sprint_asociado=sp,prioridad=2).exclude(id__in=releases).count()
            alta = f.user_stories.filter(sprint_asociado=sp,prioridad=1).exclude(id__in=releases).count()
            return render_to_response('proyecto/kanban_proyecto.html',{
                    'fs': k,'baja':baja,'media':media,'alta':alta,'releases':releases,'actividades':acti,'sp':sp,'flujo':f},context_instance=RequestContext(request))
            
@login_required(login_url= URL_LOGIN)
def cambiar_estado(request):
    if request.is_ajax():
        # variables recibidas
        i = request.GET['k'] # kanban
        ut = us.objects.get(id=i)
        k = kanban.objects.get(us=ut)
        t = k.fluj.actividades.all().count()
           
        total = 0
        prioridad = ut.prioridad
        est = k.estado
        act = k.actividad
        f = flujo.objects.get(id=k.fluj.id)
        ust= f.user_stories.all()
        proyecto_us= ut.proyecto_asociado
        proyect = proyecto.objects.get(id=proyecto_us.id)
        sp= ut.sprint_asociado
        
        ord= act.order +1
        ult = k.fluj.actividades.all().order_by('-order')[0]
        comentarios = ut.comentarios.all().count()
        releases = kanban.objects.filter(us__in=ust,fluj=k.fluj,actividad=ult,estado='de').order_by('prioridad')
        baja = f.user_stories.filter(prioridad=3).exclude(id__in=releases).count()
        media = f.user_stories.filter(prioridad=2).exclude(id__in=releases).count()
        alta = f.user_stories.filter(prioridad=1).exclude(id__in=releases).count()
        
        
        # condiciones antes de cambiar de estado
        if ut.prioridad == '3':
            if alta>baja or media>baja:
                l = {'cambiar': 'no','mensaje':'User Story con prioridad baja.'}
                return HttpResponse(json.dumps(l))
            else:
                pass
        elif ut.prioridad == '2':
            if alta>=media:
                l = {'cambiar': 'no','mensaje':'User Story con prioridad media.'}
                return HttpResponse(json.dumps(l))
        
        if comentarios == 0:
            l = {'cambiar': 'no','mensaje':'User Story debe tener al menos un comentario para el cambio de estado.'}
            return HttpResponse(json.dumps(l))
        if proyect.sprint_actual == '':
            
            proyect.sprint_actual = sp.id
            proyect.fecha_inicio =datetime.date.today()
            
            proyect.save()
            spa = sprint.objects.get(id=sp.id)
            spa.fecha_inicio= datetime.date.today()
            spa.save()
            if est == 'td':
                kanban.objects.filter(us=ut).update(estado='dg')
                est = 'dg'
            elif est == 'dg':
                kanban.objects.filter(us=ut).update(estado='de')
                est = 'de'
            else:
                if (ord<t):
                    act = k.fluj.actividades.get(order=ord)
                    kanban.objects.filter(id=i).update(estado='td',actividad=act)
                    est = 'td'
                    act = act
            l = {'ut':ut.nombre,'estado':est,'actividad':act.nombre,'ultimo':ult.nombre,'prioridad':prioridad,'cambiar':'si'}
            
            return HttpResponse(json.dumps(l))
        else: 
            if est == 'td':
                kanban.objects.filter(us=ut).update(estado='dg')
                est = 'dg'
                    
            elif est == 'dg':
                kanban.objects.filter(us=ut).update(estado='de')
                est = 'de'
            else:
                if (ord<t):
                    act = k.fluj.actividades.get(order=ord)
                    kanban.objects.filter(id=i).update(estado='td',actividad=act)
                    est = 'td'    
            l = {'ut':ut.nombre,'estado':est,'actividad':act.nombre,'ultimo':ult.nombre,'prioridad':prioridad,'cambiar':'si'}
            return HttpResponse(json.dumps(l))
            #print acti
            #print k.fluj.actividades.get(nombre=act)
        
            l = {'ut':ut.nombre,'estado':est,'actividad':act.nombre,'ultimo':ult.nombre,'prioridad':prioridad}
            return HttpResponse(json.dumps(l))
        
@login_required(login_url= URL_LOGIN)
def burndown_chart_view(request,id_proyecto):
    #Step 1: Create a DataPool with the data we want to retrieve.
    if request.method == 'GET':
        p = proyecto.objects.get(id=id_proyecto)
        sp = sprint.objects.filter(proyect=p)
        ctx = {'form':sp,'p':p}
        
        return render_to_response('proyecto/burndownchart.html',ctx,context_instance=RequestContext(request))
    
@csrf_exempt
def volver_actividad_view(request):
    if request.is_ajax():
        
        cambiar = 'no'
        mensaje = 'No se puede volver a una actividad superior'
        acti_id = request.POST.get('acti_id') 
        
        us_id =  request.POST.get('us')
        actividad_a_pasar = actividad.objects.get(id=int(acti_id))
        user_story_rel = us.objects.get(id=int(us_id))
        proyecto_rel = proyecto.objects.get(id=user_story_rel.proyecto_asociado.id)
        print request.user
        try:
            e =Equipo.objects.get(proyect=proyecto_rel,miembro=request.user)
            print e.rol
            print e.miembro
            if e.rol.name == 'Scrum' or request.user.is_staff:
                print 'aa'
                kanban_rel = kanban.objects.get(us=user_story_rel)
                actividad_anterior = actividad.objects.get(id=kanban_rel.actividad.id)
                print actividad_a_pasar.order
                print actividad_anterior.order
                if(actividad_a_pasar.order<=actividad_anterior.order):
                    kanban_rel.actividad = actividad_a_pasar
                    kanban_rel.estado = 'td'
                    kanban_rel.save()
                    cambiar = 'si'
                
            else:
                print 'aa'
                mensaje= 'no tiene permisos necesarios. Consulte con el Scrum Master'
            
        except:
            pass
        print mensaje
        l = {'cambiar':cambiar,'mensaje':mensaje,'ut':user_story_rel.nombre,'actividad':actividad_a_pasar.nombre}
        return HttpResponse(json.dumps(l))