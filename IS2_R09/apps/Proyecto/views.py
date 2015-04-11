#!/usr/bin/python
# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from IS2_R09.apps.Proyecto.forms import proyecto_form, equipo_form,\
    cantidad_form,modificar_form,consultar_form,buscar_proyecto_form
from IS2_R09.apps.Proyecto.models import proyecto,Equipo
from django.template.context import RequestContext
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User

# Create your views here.

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
                return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
            else:
                proyectos = proyecto.objects.filter(miembro=request.user)
                ctx={'proyectos':proyectos,'mensaje':'Proyecto creado','form':buscar_proyecto_form()}
                return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('proyecto/crear_proyecto.html',ctx,context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------------------------------------------------
def asignar_equipo_view(request,id_proyecto):
    '''Vista que controla la asignacion de usuario al equipo de un proyecto'''
    p = proyecto.objects.get(pk=id_proyecto)
    c= cantidad_form()
    equipo_formset = modelformset_factory(Equipo, form=equipo_form)
    if request.method == 'POST':
        formset= equipo_formset(request.POST)
        if formset.is_valid():
            formset.save()
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
            print 'HERE'
            cantidad= c.cleaned_data['cantidad']
            print c['cantidad'].value()
            equipo_formset = modelformset_factory(Equipo,form=equipo_form,extra=int(cantidad))
            formset= equipo_formset(queryset=Equipo.objects.none())
            for f in formset:
                f.fields['proyect'].initial= p
                f.fields['miembro'].queryset= User.objects.exclude(id__in=p.miembro.all())
            ctx = {'form':formset,'p':p.id}
            return render_to_response('proyecto/asignar_equipo.html',ctx,context_instance=RequestContext(request))
        
    ctx = {'aux':c,'p':p.id}
    return render_to_response('proyecto/asignar_equipo.html',ctx,context_instance=RequestContext(request))

def modificar_proyecto_view(request,id_proyecto):
    if request.method == 'POST':
        proyect = proyecto.objects.get(id=id_proyecto)
        form = modificar_form(request.POST,instance=proyect)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                proyectos = proyecto.objects.all()
                ctx={'proyectos':proyectos,'mensaje':'Proyecto modificado','form':buscar_proyecto_form()}
                return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
            else:
                proyectos = proyecto.objects.filter(miembro=request.user)
                ctx={'proyectos':proyectos,'mensaje':'Proyecto Modificado','form':buscar_proyecto_form()}
                return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
    
    if request.method=='GET':
        proyect = proyecto.objects.get(id=id_proyecto)
        form = modificar_form(instance= proyect)
        ctx = {'form':form}
        return render_to_response('proyecto/modificar_proyecto.html',ctx,context_instance=RequestContext(request))
    proyect = proyecto.objects.get(id=id_proyecto)
    form = modificar_form(instance= proyect)
    ctx = {'form':form}
    return render_to_response('proyecto/modificar_proyecto.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
def eliminar_proyecto_view(request,id_proyecto):
    '''vista que controla la eliminacion de usuarios del sistema'''
    proyect = proyecto.objects.get(pk=id_proyecto)
    if request.method == 'POST':
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
def consultar_proyecto_view(request,id_proyecto):
    if request.method=='GET':
        proyect = proyecto.objects.get(id=id_proyecto)
        equipo = proyect.miembro.all()
        print equipo
        form = consultar_form(instance= proyect)
        form.fields['miembro'].queryset=proyect.miembro.all()
        ctx = {'form':form}
        return render_to_response('proyecto/consultar_proyecto.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
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

