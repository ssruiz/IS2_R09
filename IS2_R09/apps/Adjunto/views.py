'''
Created on 30/4/2015

@author: Melissa Bogado, Samuel Ruiz, Rafael Ricardo
'''
from django.shortcuts import render_to_response
from IS2_R09.apps.Adjunto.forms import adjunto_form
from IS2_R09.apps.Adjunto.forms import consultar_adjunto_form
from IS2_R09.apps.Adjunto.forms import modificar_adjunto_form
from IS2_R09.apps.Adjunto.models import adjunto
from django.template.context import RequestContext

# Create your views here.

def adm_adjunto_view(request):
    """Vista que controla la interfaz de administracion de adjuntos"""
    adjuntos = adjunto()
    if request.user.is_staff:
        """Si el usuario es administrador se le listan todos los adjuntos"""
        adjuntos = adjunto.objects.all()
        ctx = {'adjuntos':adjuntos}
        return render_to_response('adjunto/adm_adjunto.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------

def crear_adjunto_view(request):
    """Vista que controla creacion de Adjuntos"""
    form = adjunto_form()
    if request.method == 'POST':
        form = adjunto_form(request.POST)
        if form.is_valid():
            form.save()
            ctx = {}
            return render_to_response('adjunto/adm_adjunto.html', ctx, context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('adjunto/crear_adjunto.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------
def modificar_adjunto_view(request, id_adjunto):
    a = adjunto.objects.get(id=id_adjunto)
    ad_form = adjunto_form()
    if request.method == 'POST':
        if request.FILES:
            ad_form = adjunto_form(request.POST, instance=a)
        # print ad_form.nombre
            if ad_form.is_valid():
            # formulario validado correctamente,
                actual = a.adjunto
                actual.save()
                i = ad_form.save()
                return render_to_response('adjunto/adm_adjunto.html', {'mensaje': 'Adjunto Modificado.', 'adjuntos':adjunto.objects.all(), 'icono':'icon-yes.gif'}, context_instance=RequestContext(request))
        else:
            ad_form = adjunto_form(request.POST, instance=a)
            if ad_form.is_valid():
            # formulario validado correctamente
                actual = a.adjunto
                actual.save()
                i = ad_form.save()
                return render_to_response('adjunto/adm_adjunto.html', {'mensaje': 'Adjunto Modificado.', 'adjuntos':adjunto.objects.filter(is_active=True), 'icono':'icon-yes.gif'}, context_instance=RequestContext(request))
    if request.method == 'GET':
        ad_form = adjunto_form(initial={
                                         'nombre':a.nombre,
                                         'descripcion':a.descripcion,
                                         'version':a.version,
                                         'comentario_commit':a.comentario_commit,
                                         'archivo':a.archivo,
                                         })
        ctx = {'ad_form': adjunto_form}
        return render_to_response('adjunto/modificar_adjunto.html', ctx, context_instance=RequestContext(request))
    return render_to_response('adjunto/modificar_adjunto.html', { 'ad_form': adjunto_form }, context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------
def eliminar_adjunto_view(request, id_adjunto):
    """Vista que controla la eliminacion de usuarios del sistema"""
    ad = adjunto.objects.get(pk=id_adjunto)
    if request.method == 'POST':
        ad = adjunto.objects.get(pk=id_adjunto)
        ad.delete()
        adjuntos = adjunto.objects.all()
        ctx = {'mensaje': 'Adjunto Eliminado', 'adjuntos':adjuntos}
        return render_to_response('adjunto/adm_adjunto.html', ctx, context_instance=RequestContext(request))
    ctx = {'adjunto': adjunto}
    return render_to_response('adjunto/eliminar_adjunto.html', ctx, context_instance=RequestContext(request))


#----------------------------------------------------------------------------------------------------------------
def consultar_adjunto_view(request, id_adjunto):
    c_form = consultar_adjunto_form()
    if request.method == 'GET':
        a = adjunto.objects.get(pk=id_adjunto)
        c_form = consultar_adjunto_form(initial={
                                        'id':a.id_adjunto,
                                         'nombre':a.nombre,
                                         'descripcion':a.descripcion,
                                         'version':a.version,
                                         'comentario_commit':a.comentario_commit,
                                         'archivo':a.archivo,
                                         })
    ctx = {'form':c_form}
    return render_to_response('adjunto/consultar_adjunto.html', ctx, context_instance=RequestContext(request))
    ctx = {'form':c_form}
    return render_to_response('adjunto/consultar_adjunto.html', ctx, context_instance=RequestContext(request))

#------------------------------------------------------------------------------------------------------------------
