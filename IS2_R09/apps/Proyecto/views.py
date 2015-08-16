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
import reportlab
from reportlab.pdfgen import canvas, textobject
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen.pycanvas import Canvas
from reportlab.rl_config import canvas_basefontname
from reportlab.lib.units import inch
from IS2_R09.apps.Sprint.forms import sprint_form
from django.db.models.aggregates import Sum
from reportlab.platypus.doctemplate import SimpleDocTemplate
from _io import BytesIO
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.axes import XCategoryAxis
from reportlab.platypus.flowables import Spacer
from reportlab.platypus.tables import Table
from reportlab.lib import colors
from IS2_R09.apps.Charts.models import charts
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from django import forms


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
        
        if not request.user.is_staff:
            ctx = {'motivo': 'crear'}
            return render_to_response('proyecto/no_permiso_proyecto.html',ctx,context_instance=RequestContext(request))
        
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
        
        if Equipo.objects.filter(proyect=proyect,miembro=request.user).exists():
            e = Equipo.objects.get(proyect=proyect,miembro=request.user)
            if not e.rol.name == 'Scrum':
                ctx = {'proyecto': proyect,'motivo': 'modificar'}
                return render_to_response('proyecto/no_permiso_proyecto.html',ctx,context_instance=RequestContext(request))
                
        elif not request.user.is_staff:
            ctx = {'proyecto': proyect,'motivo': 'modificar'}
            return render_to_response('proyecto/no_permiso_proyecto.html',ctx,context_instance=RequestContext(request))
                
            
            
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
        if Equipo.objects.filter(proyect=proyect,miembro=request.user).exists():
            e = Equipo.objects.get(proyect=proyect,miembro=request.user)
            if not e.rol.name == 'Scrum':
                ctx = {'proyecto': proyect,'motivo': 'eliminar'}
                return render_to_response('proyecto/no_permiso_proyecto.html',ctx,context_instance=RequestContext(request))
                
        elif not request.user.is_staff:
            ctx = {'proyecto': proyect,'motivo': 'eliminar'}
            return render_to_response('proyecto/no_permiso_proyecto.html',ctx,context_instance=RequestContext(request))
        
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
        
        ctx = {'form':form,'list':roles,'ust':ust,'cliente':client,'flujos':flujos,'sprints':sprints}
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
            ust = us.objects.filter(proyecto_asociado=pr,sprint_asociado__finalizado='no',release_asociado=None).order_by('prioridad')
            
            releases = kanban.objects.filter(us__in=ust,fluj=fj,actividad=ult,estado='de').order_by('prioridad')
            k= kanban.objects.filter(us__in=ust,fluj=fj).order_by('prioridad')
            print f
            baja = f.user_stories.filter(prioridad=3).exclude(id__in=releases).count()
            media = f.user_stories.filter(prioridad=2).exclude(id__in=releases).count()
            alta = f.user_stories.filter(prioridad=1).exclude(id__in=releases).count()
            return render_to_response('proyecto/kanban_proyecto.html',{
                    'fs': k,'baja':baja,'media':media,'alta':alta,'releases':releases,'actividades':acti,'sp':'Ninguno en desarrollo','flujo':f,'ultimo':ult.nombre},context_instance=RequestContext(request))
        else:
            sp= sprint.objects.get(id=pr.sprint_actual)
            ust = f.user_stories.filter(sprint_asociado=sp,release_asociado=None).order_by('prioridad')
            
            #releases = kanban.objects.filter(us__in=ust,fluj=fj,actividad=ult,estado='de').order_by('prioridad')
            releases = f.user_stories.filter(sprint_asociado=sp,release_asociado__lanzado='no').exclude(release_asociado=None).order_by('prioridad')
            k= kanban.objects.filter(us__in=ust,fluj=fj).order_by('prioridad')
            #baja = f.user_stories.filter(sprint_asociado=sp,prioridad=3).exclude(id__in=releases).count()
            #media = f.user_stories.filter(sprint_asociado=sp,prioridad=2).exclude(id__in=releases).count()
            #alta = f.user_stories.filter(sprint_asociado=sp,prioridad=1).exclude(id__in=releases).count()
            return render_to_response('proyecto/kanban_proyecto.html',{
                    'fs': k,'releases':releases,'actividades':acti,'sp':sp,'flujo':f,'ultimo':ult.nombre},context_instance=RequestContext(request))
            
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
        releases = f.user_stories.filter(sprint_asociado=sp,release_asociado__lanzado='si').exclude(release_asociado=None).order_by('prioridad')
        #releases = kanban.objects.filter(us__in=ust,fluj=k.fluj,actividad=ult,estado='de').order_by('prioridad')
        baja = f.user_stories.filter(prioridad=3).exclude(id__in=releases).count()
        media = f.user_stories.filter(prioridad=2).exclude(id__in=releases).count()
        alta = f.user_stories.filter(prioridad=1).exclude(id__in=releases).count()
        cambiar='si'
        mensaje=''
        # condiciones antes de cambiar de estado
        #------------------------------------------------------------------------------
        #El proyecto debe estar con estado iniciado
        estado_proyecto = proyect.estado
        estado_proyecto = estado_proyecto.lower()
        if estado_proyecto!= 'iniciado':
            l = {'cambiar': 'no','mensaje':'Proyecto aun no iniciado.'}
            return HttpResponse(json.dumps(l))
        #------------------------------------------------------------------------------
        # El usuario debe estar asignado al user story, ser scrum master o administrador
        if not us.objects.filter(usuario_asignado=request.user).exists():
            if Equipo.objects.filter(proyect=proyect,miembro=request.user).exists():
                e = Equipo.objects.get(proyect=proyect,miembro=request.user)
                if not e.rol.name == 'Scrum' or not request.user.is_staff:
                    l = {'cambiar': 'no','mensaje':'No esta asignado a este User Story.'}
                    return HttpResponse(json.dumps(l))
            elif not request.user.is_staff:
                l = {'cambiar': 'no','mensaje':'No esta asignado a este User Story.'}
                return HttpResponse(json.dumps(l))
            
        #------------------------------------------------------------------------------    
        # no deben existir user stories con prioridades mayores
        
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
        #------------------------------------------------------------------------------
        # el user  story debe tener al menos un comentario
        if comentarios == 0:
            l = {'cambiar': 'no','mensaje':'User Story debe tener al menos un comentario para el cambio de estado.'}
            return HttpResponse(json.dumps(l))
        
        #------------------------------------------------------------------------------
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
                else:
                    cambiar='no'
                    mensaje='No se puede cambiar. US en ultima actividad.' 
            l = {'ut':ut.nombre,'estado':est,'actividad':act.nombre,'ultimo':ult.nombre,'prioridad':prioridad,'cambiar':cambiar,'mensaje':mensaje}
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
        print us.objects.filter(id=us_id,usuario_asignado=request.user)
        if not us.objects.filter(id=us_id,usuario_asignado=request.user).exists():
            if Equipo.objects.filter(proyect=proyecto_rel,miembro=request.user).exists():
                e = Equipo.objects.get(proyect=proyecto_rel,miembro=request.user)
                print e.rol.name
                print e.miembro
                if not e.rol.name == 'Scrum':
                    l = {'cambiar': 'no','mensaje':'No posee permisos de Scrum master para modificar User Story.'}
                    return HttpResponse(json.dumps(l))
            elif not request.user.is_staff:
                l = {'cambiar': 'no','mensaje':'No posee permisos para modificar User Story.'}
                return HttpResponse(json.dumps(l))
        else:
            e = Equipo.objects.get(proyect=proyecto_rel,miembro=request.user)
            if not e.rol.name == 'Scrum':
                l = {'cambiar': 'no','mensaje':'No posee permisos de Scrum master para regresar a un actividad al User Story.'}
                return HttpResponse(json.dumps(l))
            elif not request.user.is_staff:
                l = {'cambiar': 'no','mensaje':'No posee permisos para regresar a un actividad al User Story.'}
                return HttpResponse(json.dumps(l))
            
        
        try:
            if Equipo.objects.filter(proyect=proyecto_rel,miembro=request.user).exists():
                e =Equipo.objects.get(proyect=proyecto_rel,miembro=request.user)
                if e.rol.name == 'Scrum':
                    print 'aa'
                    kanban_rel = kanban.objects.get(us=user_story_rel)
                    print kanban_rel
                    actividad_anterior = actividad.objects.get(id=kanban_rel.actividad.id)
                    print actividad_a_pasar.order
                    print actividad_anterior.order
                    print 'aass'
                    if(actividad_a_pasar.order<=actividad_anterior.order):
                        kanban_rel.actividad = actividad_a_pasar
                        kanban_rel.estado = 'td'
                        kanban_rel.save()
                        cambiar = 'si'
            elif request.user.is_staff:
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
                mensaje= 'no tiene permisos necesarios. Consulte con el Scrum Master'
            
        except:
            pass
        l = {'cambiar':cambiar,'mensaje':mensaje,'ut':user_story_rel.nombre,'actividad':actividad_a_pasar.nombre}
        return HttpResponse(json.dumps(l))

def reporte_view(request,id_proyecto):
    proyect= proyecto.objects.get(id=id_proyecto)
    response = HttpResponse(content_type='application/pdf')
    fecha = datetime.date.today()
    response['Content-Disposition'] = 'attachment; filename="reporte_%s_%s.pdf"' %(proyect.nombre,fecha)
    ust = us.objects.filter(proyecto_asociado=proyect)
    equipo = Equipo.objects.filter(proyect=proyect)
    sprints = sprint.objects.filter(proyect=proyect)
    
    # Create the PDF object, using the response object as its "file."
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    pdf = []
    '''
    drawing = Drawing(600, 300)
    lc = HorizontalLineChart()
    lc.x = 50
    lc.y = 50
    lc.height = 200
    lc.width = 400
    lc.data = [(2,3),(3,3)]
    lc.joinedLines = 1
    catNames ='Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
    lc.categoryAxis.categoryNames = catNames

    lc.categoryAxis.labels.boxAnchor = 'n'
    lc.valueAxis.valueMin = 0
    lc.valueAxis.valueMax = 10
    lc.valueAxis.valueStep = 5
    lc.lines[0].strokeWidth = 2
    lc.lines[1].strokeWidth = 1.5
    drawing.add(lc)
    styles = getSampleStyleSheet()
    header = Paragraph("<i>Reporte de Proyecto</i>", styles['Title'])
    clientes.append(header)
    clientes.append(drawing)
    '''
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name = "listas", leftIndent=5))
    header = Paragraph("<i>Reporte de Proyecto</i>", styles['Title'])
    pdf.append(header) 
    pdf.append(Spacer(0,20))
    pdf.append(Paragraph("<b>Nombre Proyecto</b>: %s" %(proyect.nombre), styles['Normal']))
    pdf.append(Spacer(0,10))
    pdf.append(Paragraph("<b>Equipo:</b>", styles['Normal']))
    pdf.append(Spacer(0,10))
    
    for t in equipo:
        pdf.append(Paragraph("    * %s - %s" %(t.miembro,t.rol), styles['listas']))
        pdf.append(Spacer(0,5))
    pdf.append(Spacer(0,5))    
    pdf.append(Paragraph('<b>Cantidad de Sprints: </b>%s' %(sprints.count()),styles['Normal']))
    pdf.append(Spacer(0,10))
    pdf.append(Paragraph('<b>Tiempo estimado Total de sprints(horas): </b>%s' %(sprints.aggregate(Sum('tiempo_estimado')).values()[0]),styles['Normal']))
    pdf.append(Spacer(0,10))
    pdf.append(Paragraph('<b>Tiempo trabajado en Total de sprints(horas): </b>%s' %(sprints.aggregate(Sum('tiempo_total')).values()[0]),styles['Normal']))
    pdf.append(Spacer(0,10))
    
    
    datos = [('Usuario','Trabajo Realizado','Trabajo Pendiente')]
    print proyect.sprint_actual
    for t in equipo:
        print t.miembro
        if us.objects.filter(proyecto_asociado=proyect,usuario_asignado=t.miembro).exists():
            usts = us.objects.filter(proyecto_asociado=proyect,usuario_asignado=t.miembro)
            t_total= usts.aggregate(Sum('tiempo_trabajado')).values()[0]
            t_estimado = usts.aggregate(Sum('tiempo_estimado')).values()[0]
            t_pendiente = t_total - t_estimado 
            datos.append([t.miembro,t_total,t_pendiente])
        
    tabla = Table(data=datos,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                       ])
    pdf.append(Paragraph('<b>Tabla de trabajos por usuarios: </b>' ,styles['Normal']))
    pdf.append(Spacer(0,15))
    pdf.append(tabla)
    pdf.append(Spacer(0,15))
    ust_proyecto = us.objects.filter(proyecto_asociado=proyect).order_by('prioridad')
    pdf.append(Paragraph('<b>Lista de User Stories del proyecto. </b>' ,styles['Normal']))
    pdf.append(Spacer(0,10))
    for u in ust_proyecto:
        pdf.append(Paragraph('<b>    *US</b>: %s <b>Prioridad:</b> %s ' %(u,u.get_prioridad_display()),styles['listas']))
        pdf.append(Spacer(0,5))
    pdf.append(Spacer(0,5))
    
    #------------------ Graficos -----------------
    pdf.append(Paragraph('<b>Grafico</b>.' ,styles['Normal']))
    
    drawing = Drawing(600, 300)
    lc = LinePlot()
    lc.x = 50
    lc.y = 50
    lc.height = 200
    lc.width = 400
    lc.joinedLines = 1
    lc.lines[0].symbol = makeMarker('FilledCircle')
    lc.lines[1].symbol = makeMarker('Circle')
    lc.lines[0].strokeWidth = 2
    lc.lines[1].strokeWidth = 1.5
    lc.xValueAxis.valueMin = 0
    lc.xValueAxis.valueMax = 5
    lc.yValueAxis.valueMin=0
    lc.strokeColor = colors.black
    lc.lineLabelFormat = '%2.1f'
    lc.xValueAxis.labelTextFormat ='%2.1f'
    datos_grafico = []
    value_max=0
    for s in sprints:
        data = []
        tt= s.tiempo_estimado
        dd = int(tt/24)
        
        if charts.objects.filter(proyect=proyect,sprint_actual=s).exists():
            puntos = charts.objects.filter(proyect=proyect,sprint_actual=s)
    
            ejex = []
            ejey = []
            t = [[1,tt],[dd,0]]
            for c in puntos:
                if(c.ejey>value_max):
                    value_max=c.ejey
                    lc.yValueAxis.valueMax=value_max+50
                
                data.append((c.ejex,c.ejey))
                
            
                print data[0]
            datos_grafico.append(data)

    lc.data= datos_grafico
    drawing.add(lc)
    pdf.append(drawing)
    
    #---- Backlog Sprint --------
    
    if proyect.sprint_actual != '':
        sprint_act= sprint.objects.get(id=proyect.sprint_actual)
        ust_proyecto = us.objects.filter(proyecto_asociado=proyect,sprint_asociado=sprint_act,release_asociado=None).order_by('prioridad')
        pdf.append(Paragraph('<b>Lista de User Stories del proyecto (Sprint Actual). </b>' ,styles['Normal']))
        pdf.append(Spacer(0,10))
        for u in ust_proyecto:
            pdf.append(Paragraph('<b>    *US</b>: %s <b>Prioridad:</b> %s ' %(u,u.get_prioridad_display()),styles['listas']))
            pdf.append(Spacer(0,5))
        pdf.append(Spacer(0,5))
    else:
        pdf.append(Paragraph('<b>Lista de User Stories del proyecto (Sprint Actual). </b>' ,styles['Normal']))
        pdf.append(Paragraph('<b>Ningun Sprint en desarrollo actualmente . </b>' ,styles['listas']))
        
        pdf.append(Spacer(0,10))
        
    '''
    p = canvas.Canvas(response)
    p.drawCentredString(255, 800, 'Reporte de Proyecto', None)
    
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    to= canvas.Canvas.beginText(p, 0, 0)
    to.setTextOrigin(100, 780)
    charspace = 0
    to.setCharSpace(charspace)
    to.setLeading(15)
    to.textOut('')
    to.textLine("Nombre Proyecto: %s" %(proyect.nombre))
    charspace = charspace +0.5
    to.setCharSpace(charspace)
    
    to.textLine("Equipo:" )
    to.textOut('')
    
    for t in equipo:
        to.textLine("    * %s - %s" %(t.miembro,t.rol))
    to.textLine('')
    to.textLine('Cantidad de Sprints: %s' %(sprints.count()))
    to.textLine('Tiempo estimado total de sprints(horas): %s' %(sprints.aggregate(Sum('tiempo_estimado')).values()[0]))
    to.textLine('Tiempo trabajado en total de sprints(horas): %s' %(sprints.aggregate(Sum('tiempo_total')).values()[0]))
    to.textLine('')
    to.textLine('Trabajo por miembro de equipo.')
    to.textLine('')
    to.setLeading(20)
    for t in equipo:
        
        usts = us.objects.filter(proyecto_asociado=proyect,usuario_asignado=t.miembro)
        print usts
        to.textLine('Usuario: %s' %(t.miembro))
        t_total= usts.aggregate(Sum('tiempo_trabajado')).values()[0]
        t_estimado = usts.aggregate(Sum('tiempo_estimado')).values()[0]
        t_pendiente = t_total - t_estimado 
        to.textOut('')
        to.textLine('    Trabajo pendiente(horas): %s Trabajo realizado(horas): %s' %(t_pendiente,t_total))
        to.textOut('')
    ust_proyecto = us.objects.filter(proyecto_asociado=proyect).order_by('prioridad')
    to.textLine('')
    to.textLine('Lista de User Stories del proyecto.')
    to.textOut('')
    for u in ust_proyecto:
        to.textLine('    US: %s Prioridad: %s' %(u,u.get_prioridad_display()))
    p.drawText(to)
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    '''
    doc.build(pdf)
    response.write(buff.getvalue())
    buff.close()
    return response