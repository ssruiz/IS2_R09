# -*- encoding: utf-8 -*-
'''
Created on 23/4/2015

@author: meliam
'''
from django.shortcuts import render_to_response
from IS2_R09.apps.Sprint.forms import sprint_form
from IS2_R09.apps.Sprint.forms import consultar_sprint_form
from IS2_R09.apps.Sprint.forms import buscar_sprint_form
from IS2_R09.apps.Sprint.models import sprint
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect
from IS2_R09.apps.Proyecto.models import proyecto
from IS2_R09.apps.US.models import us

# Create your views here.

def adm_sprint_view(request):
    """Vista que controla la interfaz de administracion de sprints"""
    sprints = sprint()
   
    """Si el usuario es administrador se le listan todos los sprints"""
    sprints = sprint.objects.all()
    ctx = {'sprints':sprints,'form':buscar_sprint_form()}
    return render_to_response('sprint/adm_sprint.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------

def crear_sprint_view(request):
    """Vista que controla creacion de Sprints"""
    form = sprint_form()
    if request.method == 'POST':
        form = sprint_form(request.POST)
        if form.is_valid():
            form.save()
            sprints = sprint.objects.all()
            ctx = {'sprints':sprints,'form':buscar_sprint_form()}
            return HttpResponseRedirect('/adm_sprint/', ctx)
    ctx = {'form':form}
    return render_to_response('sprint/crear_sprint.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------
def modificar_sprint_view(request, id_sprint):
    s = sprint.objects.get(id=id_sprint)
    sp_form = sprint_form()
    if request.method == 'POST':
        sp_form = sprint_form(request.POST, instance=s)
        # print sp_form.nombre
        if sp_form.is_valid():
            # formulario validado correctamente,
            sp_form.save()
            return HttpResponseRedirect('/adm_sprint/', {'mensaje': 'Sprint Modificado.', 'sprints':sprint.objects.all(), 'icono':'icon-yes.gif'})
    if request.method == 'GET':
        p = proyecto.objects.get(id=s.proyect.id)
        sp_form = sprint_form(instance=s)
        ctx = {'form': sp_form}
        return render_to_response('sprint/modificar_sprint.html', ctx, context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------
def eliminar_sprint_view(request, id_sprint):
    """Vista que controla la eliminacion de usuarios del sistema"""
    sp = sprint.objects.get(pk=id_sprint)
    if request.method == 'POST':
        sp = sprint.objects.get(pk=id_sprint)
        sp.delete()
        sprints = sprint.objects.all()
        ctx = {'mensaje': 'Sprint Eliminado', 'sprints':sprints}
        return HttpResponseRedirect('/adm_sprint/', ctx)
    ctx = {'sprint': sp}
    return render_to_response('sprint/eliminar_sprint.html', ctx, context_instance=RequestContext(request))


#----------------------------------------------------------------------------------------------------------------
def consultar_sprint_view(request, id_sprint):
    c_form = consultar_sprint_form()
    if request.method == 'GET':
        s = sprint.objects.get(pk=id_sprint)
        c_form = consultar_sprint_form(instance=s)
        ctx = {'form':c_form,'p':s.proyect}
        return render_to_response('sprint/consultar_sprint.html', ctx, context_instance=RequestContext(request))
    ctx = {'form':c_form}
    return render_to_response('sprint/consultar_sprint.html', ctx, context_instance=RequestContext(request))

#------------------------------------------------------------------------------------------------------------------
def buscar_sprint_view(request):
    b_form = buscar_sprint_form()
    if(request.method == 'POST'):
        b_form = buscar_sprint_form(request.POST)
        b_form2 = buscar_sprint_form()
        if b_form.is_valid():
            busqueda = b_form.cleaned_data['opciones']
            parametro = b_form.cleaned_data['busqueda']
            if busqueda == 'nombre':
                s = sprint.objects.filter(nombre=parametro)
                ctx = {'mensaje': 'Sprints con nombre %s' % (parametro), 'sprints':s, 'form':b_form2}
                return render_to_response('sprint/adm_sprint.html', ctx, context_instance=RequestContext(request))
    ctx = {'b_form': b_form}
    return render_to_response('sprint/buscar_sprint.html', ctx, context_instance=RequestContext(request))
