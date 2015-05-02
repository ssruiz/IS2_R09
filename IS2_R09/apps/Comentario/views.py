# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from IS2_R09.apps.US.models import us
from django.template.context import RequestContext
from IS2_R09.apps.Comentario.forms import comentario_form,\
    comentario_consulta_form
from IS2_R09.apps.Comentario.models import comentario
from django.http.response import HttpResponseRedirect
import datetime
from IS2_R09.apps.Adjunto.forms import consultar_adjunto_form
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
    ctx = {'comentario': comentario,'userid':id_us}
    return render_to_response('comentario/eliminar_comentario.html', ctx, context_instance=RequestContext(request))


#----------------------------------------------------------------------------------------------------------------
def consultar_comentario_view(request, id_comentario,id_us):
    if request.method == 'GET':
        c= comentario.objects.get(id=id_comentario)
        form = consultar_adjunto_form(instance=c)
        ctx = {'form': form,'userid':id_us}
        return render_to_response('comentario/consultar_comentario.html', ctx, context_instance=RequestContext(request))
    


