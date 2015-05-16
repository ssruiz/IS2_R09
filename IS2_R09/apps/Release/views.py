"""
Created on 15/5/2015

@author: Melissa Bogado,Samuel Ruiz, Rafael Ricardo
"""
# -*- encoding: utf-8 -*-
from IS2_R09.apps.Release.forms import release_form, consultar_release_form,buscar_release_form
from django.shortcuts import render_to_response
from IS2_R09.apps.Release.models import release
from IS2_R09.apps.Sprint.models import sprint
#from IS2_R09.apps.US.models import us
from django.template.context import RequestContext
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
import datetime

# Create your views here.
@login_required(login_url= URL_LOGIN)
def adm_release_view(request):
    ''''Vista que controla la interfaz de administracion de releases'''
    releases = release()
    if request.user.is_staff:
        '''Si el usuario es administrador se le listan todos los releases'''
        releases = release.objects.all()
        ctx={'releases':releases,'form':buscar_release_form()}
        return render_to_response('release/adm_releases.html',ctx,context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def crear_release_view(request):
    '''Vista que controla creacion de Releases'''
    form= release_form()
    if request.method == 'POST':
        form = release_form(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                releases = release.objects.all()
                ctx={'releases':releases,'mensaje':'Release Creado','form':buscar_release_form()}
                return render_to_response('release/adm_release.html',ctx,context_instance=RequestContext(request))
            else:
                releases = release.objects.filter(miembro=request.user)
                ctx={'releases':releases,'mensaje':'Release Creado','form':buscar_release_form()}
                return render_to_response('release/adm_release.html',ctx,context_instance=RequestContext(request))
    form.fields['fecha_creacion'].initial = datetime.date.today()        
    ctx = {'form':form}
    return render_to_response('release/crear_release.html',ctx,context_instance=RequestContext(request))

#------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def modificar_release_view(request,id_release):
    if request.method == 'POST':
        release = release.objects.get(id=id_release)
        form = modificar_release_form(request.POST,instance=release)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                releases = release.objects.all()
                ctx={'releases':releases,'mensaje':'Release Modificado','form':buscar_release_form()}
                return render_to_response('release/adm_release.html',ctx,context_instance=RequestContext(request))
            else:
                releases = release.objects.filter(miembro=request.user)
                ctx={'releases':releases,'mensaje':'Release Modificado','form':buscar_release_form()}
                return render_to_response('release/adm_release.html',ctx,context_instance=RequestContext(request))
    
    if request.method=='GET':
        release = release.objects.get(id=id_release)
        form = modificar_release_form(instance = release)
        ctx = {'form':form}
        return render_to_response('release/modificar_release.html',ctx,context_instance=RequestContext(request))
    release = release.objects.get(id=id_release)
    form = modificar_release_form(instance = release)
    ctx = {'form':form}
    return render_to_response('release/modificar_release.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def eliminar_release_view(request,id_release):
    '''vista que controla la eliminacion de releases del sistema'''
    release = release.objects.get(pk=id_release)
    if request.method == 'POST':
        release.delete()
        if request.user.is_staff:
                releases = release.objects.all()
                ctx={'releases':releases,'mensaje':'Release Eliminado','form':buscar_release_form()}
                return render_to_response('release/adm_release.html',ctx,context_instance=RequestContext(request))
        else:
            releases = release.objects.filter(miembro=request.user)
            ctx={'releases':releases,'mensaje':'Release Eliminado','form':buscar_release_form()}
            return render_to_response('release/adm_release.html',ctx,context_instance=RequestContext(request))
    
    ctx = {'release': release}
    return render_to_response('release/eliminar_release.html', ctx, context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def consultar_release_view(request,id_release):
    if request.method=='GET':
        release = release.objects.get(id=id_release)
#        roles = Equipo.objects.filter(proyect=proyect)
        
#        equipo = proyect.miembro.all()
        form = consultar_release_form(instance = release)
#        form.fields['miembro'].queryset=proyect.miembro.all()
#        form.fields['flujos'].queryset=proyect.flujos.all()
#        list= zip(equipo,roles)
        ctx = {'form':form,'list':list}
        return render_to_response('release/consultar_release.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def buscar_release_view(request):
    form = buscar_release_form()
    if(request.method=='POST'):
        form = buscar_release_form(request.POST)
        form2 = buscar_release_form()
        if form.is_valid():
            busqueda = form.cleaned_data['opciones']
            parametro = form.cleaned_data['busqueda']
            if busqueda == 'version':
                r = release.objects.filter(version=parametro)
                ctx = {'mensaje': 'Release Version %s' %(parametro),'releases':r,'form':form2}
                return render_to_response('release/adm_release.html', ctx, context_instance=RequestContext(request))
            elif busqueda == 'sprint_asociado':
                try:
                    s = sprint.objects.get(id_sprint=parametro)
                    r = release.objects.filter(sprint_asociado=s)
                    ctx = {'mensaje': 'Sprint %s Asociado al Release' %(s),'releases':r,'form':form2}
                    return render_to_response('proyecto/adm_proyecto.html', ctx, context_instance=RequestContext(request))
                except:
                        if request.user.is_staff:
                            releases = release.objects.all()
                            ctx={'releases':releases,'mensaje':'Sprint Asociado con ID %s no existe'%(parametro),'form':buscar_release_form()}
                            return render_to_response('release/adm_release.html',ctx,context_instance=RequestContext(request))
                        else:
                            releases = release.objects.filter(miembro=request.user)
                            ctx={'releases':releases,'mensaje':'Sprint Asociado con ID %s no existe'%(parametro),'form':buscar_release_form()}
                            return render_to_response('release/adm_release.html',ctx,context_instance=RequestContext(request))
                    
    ctx = {'form': form}
    return render_to_response('release/adm_release.html', ctx, context_instance=RequestContext(request))
