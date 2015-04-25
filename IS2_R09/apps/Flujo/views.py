# -*- encoding: utf-8 -*-

"""
    Vistas (Views)
    ==============
    
    Módulo que contiene las vistas del módulo L{Flujo<IS2_R09.apps.Flujo>}, encargadas de controlar las
    distintas operaciones aplicables al mismo.
"""

from django.shortcuts import render, render_to_response
from IS2_R09.apps.Flujo.models import flujo,actividad
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
from IS2_R09.apps.Flujo.forms import flujo_form,buscar_flujo_form,actividad_form,consultar_form
from django.contrib.redirects.models import Redirect
from django.http.response import HttpResponseRedirect

@login_required(login_url= URL_LOGIN)
def adm_flujo_view(request):
    """
        adm_flujo_view(request)
        Administración de Flujos.
        =========================
        
        Vista que controla la interfaz de administracion de flujos
        @param request: Almacena información concerniente a la consulta realizada
        como el usuario que la realiza etc.
    """
    flujos= flujo()
    if request.user.is_staff:
        flujos = flujo.objects.all()
        ctx={'flujos':flujos,'form':buscar_flujo_form()}
        return render_to_response('flujo/adm_flujo.html',ctx,context_instance=RequestContext(request))
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url= URL_LOGIN)
def crear_flujo_view(request):
    """
        crear_flujo_view(request)
        Administración de Flujos.
        =========================
        
        Vista que controla la interfaz de creación de flujos
        @param request: Almacena información concerniente a la consulta realizada
        como el usuario que la realiza etc.
    """
    form= flujo_form()
    if request.method == 'POST':
        form = flujo_form(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                flujos = flujo.objects.all()
                ctx={'flujos':flujos,'mensaje':'Flujo creado','form':buscar_flujo_form()}
                return HttpResponseRedirect('/adm_flujo/',ctx)
    ctx = {'form':form}
    return render_to_response('flujo/crear_flujo.html',ctx,context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url= URL_LOGIN)
def crear_actividad_view(request):
    """
        crear_actividad_view(request)
        Crear Actividad para Flujo.
        ===========================
        
        Vista que controla la interfaz de creación de actividades paraflujos
        @param request: Almacena información concerniente a la consulta realizada
        como el usuario que la realiza etc.
    """
    form = actividad_form()
    if request.method == 'POST':
        form = actividad_form(request.POST)
        if form.is_valid():
            form.save()
            form= flujo_form()
            ctx = {'form':form}
            return HttpResponseRedirect('/crear_flujo/',ctx)
    ctx = {'form':form}
    return render_to_response('actividad/crear_actividad.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def eliminar_flujo_view(request,id_flujo):
    """
        eliminar_flujo_view(request,id_flujo)
        Eliminación de Flujos.
        ======================
        
        Vista que controla la eliminación de flujos
        @param request: Almacena información concerniente a la consulta realizada.
        @param id_flujo: ID del flujo a eliminar.
    """
    fluj = flujo.objects.get(pk=id_flujo)
    if request.method == 'POST':
        fluj.delete()
        if request.user.is_staff:
            flujos = flujo.objects.all()
            ctx={'flujos':flujos,'form':buscar_flujo_form()}
            return HttpResponseRedirect('/adm_flujo/',ctx)
                
    ctx = {'flujo': fluj}
    return render_to_response('flujo/eliminar_flujo.html', ctx, context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------

@login_required(login_url= URL_LOGIN)
def modificar_flujo_view(request,id_flujo):
    """
        modificar_flujo_view(request,id_flujo)
        Modificación de Flujos.
        =======================
        
        Vista que controla la modificación de datos de los flujos
        @param request: Almacena información concerniente a la consulta realizada como el usuario
        que la realiza, los datos del formulario, etc.
        @param id_flujo: ID del flujo a modificar.
    """
    if request.method == 'POST':
        fluj = flujo.objects.get(id=id_flujo)
        form = flujo_form(request.POST,instance=fluj)
        if form.is_valid():
            form.save()
            flujos = flujo.objects.all()
            ctx={'flujos':flujos,'form':buscar_flujo_form()}
            return render_to_response('flujo/adm_flujo.html',ctx,context_instance=RequestContext(request))
    if request.method=='GET':
        fluj = flujo.objects.get(id=id_flujo)
        form = flujo_form(instance= fluj)
        ctx = {'form':form,'id':id_flujo}
        return render_to_response('flujo/modificar_flujo.html',ctx,context_instance=RequestContext(request))
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def crear_actividad_from_mod_view(request,id_flujo):
    """
        crear_actividad_view(request,id_flujo)
        Crear Actividad para Flujo.
        ===========================
        
        Vista que controla la interfaz de creación de actividades para flujos desde la modificacion
        @param request: Almacena información concerniente a la consulta realizada
        como el usuario que la realiza etc.
        @param id_flujo: Flujo que se estaba modificando
    """
    form = actividad_form()
    if request.method == 'POST':
        form = actividad_form(request.POST)
        if form.is_valid():
            form.save()
            fluj = flujo.objects.get(id=id_flujo)
            form = flujo_form(instance= fluj)
            ctx = {'form':form}
            return HttpResponseRedirect('/modificar/flujo/%s'%(id_flujo),ctx)
    ctx = {'form':form}
    return render_to_response('actividad/crear_actividad.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
    
@login_required(login_url= URL_LOGIN)
def consultar_flujo_view(request,id_flujo):
    """
        consultar_flujo_view(request,id_flujo)
        Consulta de Flujo.
        ==================
        
        Vista que controla la consuta de datos de los flujos
        @param request: Almacena información concerniente a la consulta realizada.
        @param id_flujo: ID del flujo a eliminar.
    """
    if request.method=='GET':
        fluj = flujo.objects.get(id=id_flujo)
        form = consultar_form(instance= fluj)
        form.fields['actividades'].queryset=fluj.actividades.all()
        ctx = {'form':form}
        return render_to_response('flujo/consultar_flujo.html',ctx,context_instance=RequestContext(request))
#------------------------------------------------------------------------------------------------------------

@login_required(login_url= URL_LOGIN)
def buscar_flujo_view(request):
    """
        buscar_flujo_view(request)
        Búsqueda de Flujos.
        ===================
        
        Vista que controla la busqueda de flujos a traves del nombre.
        @param request: Almacena información concerniente a la consulta realizada.
    """
    form = buscar_flujo_form()
    if(request.method=='POST'):
        form = buscar_flujo_form(request.POST)
        form2 = buscar_flujo_form()
        if form.is_valid():
            busqueda= form.cleaned_data['opciones']
            parametro = form.cleaned_data['busqueda']
            if busqueda== 'nombre':
                p = flujo.objects.filter(nombre=parametro)
                ctx = {'mensaje': 'Flujo con nombre %s' %(parametro),'flujos':p,'form':form2}
                return render_to_response('flujo/adm_flujo.html', ctx, context_instance=RequestContext(request))
                                
    ctx = {'form': form}
    return render_to_response('proyecto/adm_flujo.html', ctx, context_instance=RequestContext(request))
    