#!/usr/bin/python
# -*- encoding: utf-8 -*-
from IS2_R09.apps.Proyecto.forms import proyecto_form, equipo_form,cantidad_form,modificar_form,consultar_form,buscar_proyecto_form,\
    proyecto_kanban_form
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
from django.contrib.sites import requests
from django import forms
from IS2_R09.apps.Flujo.models import kanban, flujo, actividad
from IS2_R09.apps.Flujo.forms import kanban_form, kanban_form_est
from IS2_R09.apps.Notificaciones.views import notificar_asignacion_proyecto,\
    notificar_mod_proyecto, notificar_eli_proyecto
from keyring.backend import json
from django.template.loader import get_template
from IS2_R09.apps.Sprint.models import sprint
from django.core.context_processors import media
from ImageColor import str2int
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
        sprints = sprint.objects.filter(proyect=proyect)
        client = proyect.cliente
        list= zip(equipo,roles)
        ust = us.objects.filter(proyecto_asociado=id_proyecto).order_by('prioridad')
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

def ustload(request):
    if request.is_ajax():
        idf= request.GET['fluj_id']
        p = request.GET['p']
        fj= flujo.objects.get(id=idf)
        pr = proyecto.objects.get(id=p)
        f= pr.flujos.get(id=idf)
        ult = fj.actividades.all().order_by('-order')[0]
        if pr.sprint_actual == '':
            print 'hola'
            ust = f.user_stories.all().order_by('prioridad')
            releases = kanban.objects.filter(us__in=ust,fluj=fj,actividad=ult,estado='de').order_by('prioridad')
            k= kanban.objects.filter(us__in=ust,fluj=fj).exclude(us__in=ust,fluj=fj,actividad=ult,estado='de').order_by('prioridad')
            baja = f.user_stories.filter(prioridad=3).exclude(id__in=releases).count()
            media = f.user_stories.filter(prioridad=2).exclude(id__in=releases).count()
            alta = f.user_stories.filter(prioridad=1).exclude(id__in=releases).count()
            
            return render_to_response('proyecto/kanban_proyecto.html',{
                    'fs': k,'baja':baja,'media':media,'alta':alta,'releases':releases},context_instance=RequestContext(request))
        else:
            sp= sprint.objects.get(id=pr.sprint_actual)
            ust = f.user_stories.filter(sprint_asociado=sp).order_by('prioridad')
            
            releases = kanban.objects.filter(us__in=ust,fluj=fj,actividad=ult,estado='de').order_by('prioridad')
            k= kanban.objects.filter(us__in=ust,fluj=fj).exclude(us__in=ust,fluj=fj,actividad=ult,estado='de').order_by('prioridad')
            baja = f.user_stories.filter(sprint_asociado=sp,prioridad=3).exclude(id__in=releases).count()
            media = f.user_stories.filter(sprint_asociado=sp,prioridad=2).exclude(id__in=releases).count()
            alta = f.user_stories.filter(sprint_asociado=sp,prioridad=1).exclude(id__in=releases).count()
            print 'media'+ str(media)
            return render_to_response('proyecto/kanban_proyecto.html',{
                    'fs': k,'baja':baja,'media':media,'alta':alta,'releases':releases},context_instance=RequestContext(request))
            
def cambiar_estado(request):
    if request.is_ajax():
        # variables recibidas
        i = request.GET['k'] # kanban
        ust = request.GET['us'] # User Story
        act = request.GET['act'] #actividad
        est = request.GET['es']
        ht = request.GET['ht']
        k = kanban.objects.get(id=i)
        t = k.fluj.actividades.all().count()
        ut = us.objects.get(nombre=ust)
        total = 0
        prioridad = ut.prioridad
        proyecto_us= ut.proyecto_asociado
        proyect = proyecto.objects.get(id=proyecto_us.id)
        sp= ut.sprint_asociado
        acti = k.fluj.actividades.get(nombre=act)
        
        ord= acti.order +1
        ult = k.fluj.actividades.all().order_by('-order')[0]
        ult = ult.nombre
        if proyect.sprint_actual == '':
            proyect.sprint_actual = sp.id
            proyect.save()
            spa = sprint.objects.get(id=sp.id)
            if est == 'to do':
                kanban.objects.filter(id=i).update(estado='dg')
                est = 'doing'
            elif est == 'doing':
                total =int(ht)
                ut.tiempo_trabajado+= total
                spa.tiempo_total+=total
                ut.save()
                spa.save()
                kanban.objects.filter(id=i).update(estado='de')
                est = 'done'
            else:
                if (ord<t):
                    acti = k.fluj.actividades.get(order=ord)
                    kanban.objects.filter(id=i).update(estado='td',actividad=acti)
                    est = 'to do'
                    act = acti.nombre
            l = {'estado':est,'actividad':act,'ultimo':ult}
            return HttpResponse(json.dumps(l))
        else:
            if est == 'to do':
                kanban.objects.filter(id=i).update(estado='dg')
                est = 'doing'
            elif est == 'doing':
                total =int(ht)
                spa = sprint.objects.get(id=sp.id)
                ut.tiempo_trabajado+= total
                spa.tiempo_total+=total
                ut.save()
                spa.save()
                kanban.objects.filter(id=i).update(estado='de')
                est = 'done'
            else:
                if (ord<t):
                    acti = k.fluj.actividades.get(order=ord)
                    kanban.objects.filter(id=i).update(estado='td',actividad=acti)
                    est = 'to do'
                    act = acti.nombre
                else:
                    pass
                    
                    
            #print acti
            #print k.fluj.actividades.get(nombre=act)
            l = {'estado':est,'actividad':act,'ultimo':ult,'prioridad':prioridad}
            return HttpResponse(json.dumps(l))