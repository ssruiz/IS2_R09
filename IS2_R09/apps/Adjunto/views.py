'''
Created on 30/4/2015

@author: Melissa Bogado, Samuel Ruiz, Rafael Ricardo
'''
from django.shortcuts import render_to_response
from IS2_R09.apps.Adjunto.forms import adjunto_form
from IS2_R09.apps.Adjunto.forms import consultar_adjunto_form
from IS2_R09.apps.Adjunto.models import adjunto, archivoUs
from django.template.context import RequestContext
from IS2_R09.apps.US.models import us
from django.http.response import HttpResponseRedirect, HttpResponse
import datetime
from IS2_R09.apps.Proyecto.models import Equipo, proyecto
from keyring.backend import json
# Create your views here.

def adm_adjunto_view(request,id_us):
    """Vista que controla la interfaz de administracion de Adjuntos"""
    userst = us.objects.get(id=id_us)
    adjuntos = userst.adjuntos.all()
    ctx = {'adjuntos':adjuntos,'userid':id_us}
    return render_to_response('adjunto/adm_adjunto.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------

def crear_adjunto_view(request,id_us):
    """Vista que controla creacion de adjuntos"""
    form = adjunto_form()
    if request.method == 'POST':
        ust= us.objects.get(id=id_us)
        form = adjunto_form(request.POST,request.FILES)
        if form.is_valid():
            c = form.save()
            ust.adjuntos.add(c)
            ust.save()
            nextt = request.POST.get('next')
            sgte = request.META.get('HTTP_REFERER')
            place = sgte.find('next')
            print place
            print sgte
            if place != -1 :
                place += 5
                sgte = '/' + sgte[place:]
            
                return HttpResponseRedirect(sgte)
            return HttpResponseRedirect('/adm_adjunto/%s'%(id_us))
    ctx = {'form':form,'userid':id_us}
    return render_to_response('adjunto/crear_adjunto.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------
def modificar_adjunto_view(request, id_adjunto,id_us):
    a = adjunto.objects.get(id=id_adjunto)
    ad_form = adjunto_form()
    if request.method == 'POST':
        if request.FILES:
            ad_form = adjunto_form(request.POST,request.FILES, instance=a)
        # print ad_form.nombre
            if ad_form.is_valid():
            # formulario validado correctamente,
                ad_form.save()
                return HttpResponseRedirect('/adm_adjunto/%s'%(id_us))
        else:
            ad_form = adjunto_form(request.POST, instance=a)
            if ad_form.is_valid():
            # formulario validado correctamente
                ad_form.save()
                return HttpResponseRedirect('/adm_adjunto/%s'%(id_us))
    
    if request.method == 'GET':
        ad_form = adjunto_form(instance=a)
        ctx = {'form': ad_form,'userid':id_us}
        return render_to_response('adjunto/modificar_adjunto.html', ctx, context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------
def eliminar_adjunto_view(request,id_adjunto,id_us):
    """Vista que controla la eliminacion de usuarios del sistema"""
    a = adjunto.objects.get(id=id_adjunto)
    userst = us.objects.get(id=id_us)
    if request.method == 'POST':
        a.archivo.delete()
        a.delete()
        adjuntos = userst.adjuntos.all()
        ctx = {'adjuntos':adjuntos,'userid':id_us}
        return HttpResponseRedirect('/adm_adjunto/%s'%(id_us),ctx)
    ctx = {'adjunto': adjunto,'userid':id_us}
    return render_to_response('adjunto/eliminar_adjunto.html', ctx, context_instance=RequestContext(request))


#----------------------------------------------------------------------------------------------------------------
def consultar_adjunto_view(request, id_adjunto,id_us):
    if request.method == 'GET':
        a= adjunto.objects.get(id=id_adjunto)
        form = consultar_adjunto_form(instance=a)
        ctx = {'form': form,'userid':id_us,'archivo':a.archivo.url}
        return render_to_response('adjunto/consultar_adjunto.html', ctx, context_instance=RequestContext(request))
    

def permisos_agregar_view(request):
    if request.is_ajax():
        i = request.GET['k'] # kanban
        proyecto_rel = proyecto.objects.get(id=i)
        if not us.objects.filter(usuario_asignado=request.user).exists():
            if Equipo.objects.filter(proyect=proyecto_rel,miembro=request.user).exists():
                e = Equipo.objects.get(proyect=proyecto_rel,miembro=request.user)
                if not e.rol.name == 'Scrum' or not request.user.is_staff:
                    l = {'permiso': 'no','mensaje':'No esta asignado al User Story o no posee permisos de Scrum master para agregar archivos .'}
                    return HttpResponse(json.dumps(l))
            elif not request.user.is_staff:
                l = {'permiso': 'no','mensaje':'No posee permisos para modificar User Story.'}
                return HttpResponse(json.dumps(l))
        l = {'permiso': 'si','mensaje':'Posee permisos para modificar User Story.'}
        return HttpResponse(json.dumps(l))
        #------------------------------------------------------------------------------    
        
