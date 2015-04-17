# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from IS2_R09.apps.Flujo.models import flujo,actividad
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
from IS2_R09.apps.Flujo.forms import flujo_form,buscar_flujo_form,actividad_form,consultar_form
from django.contrib.redirects.models import Redirect
from django.http.response import HttpResponseRedirect

# Create your views here.
def adm_flujo_view(request):
    ''''Vista que controla la interfaz de administracion de flujos'''
    flujos= flujo()
    if request.user.is_staff:
        '''Si el usuario es administrador se le listan todos los proyectos'''
        flujos = flujo.objects.all()
        ctx={'flujos':flujos,'form':buscar_flujo_form()}
        return render_to_response('flujo/adm_flujo.html',ctx,context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def crear_flujo_view(request):
    '''Vista que controla creacion de Flujos'''
    form= flujo_form()
    if request.method == 'POST':
        form = flujo_form(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                flujos = flujo.objects.all()
                ctx={'flujos':flujos,'mensaje':'Flujo creado','form':buscar_flujo_form()}
                return render_to_response('flujo/adm_flujo.html',ctx,context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('flujo/crear_flujo.html',ctx,context_instance=RequestContext(request))

@login_required(login_url= URL_LOGIN)
def crear_actividad_view(request):
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
    '''vista que controla la eliminacion de flujos del sistema'''
    fluj = flujo.objects.get(pk=id_flujo)
    if request.method == 'POST':
        fluj.delete()
        if request.user.is_staff:
            flujos = flujo.objects.all()
            ctx={'flujos':flujos,'form':buscar_flujo_form()}
            return render_to_response('flujo/adm_flujo.html',ctx,context_instance=RequestContext(request))
                
    ctx = {'flujo': fluj}
    return render_to_response('flujo/eliminar_flujo.html', ctx, context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------

@login_required(login_url= URL_LOGIN)
def modificar_flujo_view(request,id_flujo):
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
        ctx = {'form':form}
        return render_to_response('flujo/modificar_flujo.html',ctx,context_instance=RequestContext(request))
    
@login_required(login_url= URL_LOGIN)
def consultar_flujo_view(request,id_flujo):
    if request.method=='GET':
        fluj = flujo.objects.get(id=id_flujo)
        form = consultar_form(instance= fluj)
        form.fields['actividades'].queryset=fluj.actividades.all()
        ctx = {'form':form}
        return render_to_response('flujo/consultar_flujo.html',ctx,context_instance=RequestContext(request))
#------------------------------------------------------------------------------------------------------------

@login_required(login_url= URL_LOGIN)
def buscar_flujo_view(request):
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
    