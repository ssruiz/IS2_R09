from django.shortcuts import render_to_response
from IS2_R09.apps.Sprint.forms import sprint_form
from IS2_R09.apps.Sprint.forms import consultar_sprint_form
from IS2_R09.apps.Sprint.forms import buscar_sprint_form
from IS2_R09.apps.Sprint.models import sprint
from django.template.context import RequestContext

# Create your views here.

def adm_sprint_view(request):
    """Vista que controla la interfaz de administracion de sprints"""
    sprints = sprint()
    if request.user.is_staff:
        """Si el usuario es administrador se le listan todos los sprints"""
        sprints = sprint.objects.all()
        ctx = {'sprints':sprints}
        return render_to_response('sprint/adm_sprint.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------

def crear_sprint_view(request):
    """Vista que controla creacion de Sprints"""
    form = sprint_form()
    if request.method == 'POST':
        form = sprint_form(request.POST)
        if form.is_valid():
            form.save()
            ctx = {}
            return render_to_response('sprint/adm_sprint.html', ctx, context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('sprint/crear_sprint.html', ctx, context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------
def modificar_sprint_view(request, id_usuario):
    s = sprint.objects.get(id=id_sprint)
    sp_form = sprint_form()
    if request.method == 'POST':
        if request.FILES:
            sp_form = sprint_form(request.POST, instance=s)
        # print sp_form.nombre
            if sp_form.is_valid():
            # formulario validado correctamente,
                actual = s.sprint
                actual.save()
                i = sp_form.save()
                return render_to_response('sprint/adm_sprint.html', {'mensaje': 'Sprint Modificado.', 'sprints':sprint.objects.all(), 'icono':'icon-yes.gif'}, context_instance=RequestContext(request))
        else:
            sp_form = sprint_form(request.POST, instance=s)
            if sp_form.is_valid():
            # formulario validado correctamente
                actual = s.sprint
                actual.save()
                i = sp_form.save()
                return render_to_response('sprint/adm_sprint.html', {'mensaje': 'Sprint Modificado.', 'sprints':sprint.objects.filter(is_active=True), 'icono':'icon-yes.gif'}, context_instance=RequestContext(request))
    if request.method == 'GET':
        sp_form = sprint_form(initial={
                                         # 'nombre':s.nombre,
                                         'fecha_creacion':s.fecha_creacion,
                                         'fecha_inicio':s.fecha_inicio,
                                         'fecha_fin':s.fecha_fin,
					 'release_asociado':s.release_asociado,
					 'flujo_asociado':s.flujo_asociado,
                                         })
        ctx = {'sp_form': sprint_form}
        return render_to_response('sprint/modificar_sprint.html', ctx, context_instance=RequestContext(request))
    return render_to_response('sprint/modificar_sprint.html', { 'sp_form': sprint_form }, context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------
def eliminar_sprint_view(request, id_sprint):
    """Vista que controla la eliminacion de usuarios del sistema"""
    sp = sprint.objects.get(pk=id_sprint)
    if request.method == 'POST':
        sp = sprint.objects.get(pk=id_sprint)
        sp.delete()
        sprints = sprint.objects.all()
        ctx = {'mensaje': 'Sprint Eliminado', 'sprints':sprints}
        return render_to_response('sprint/adm_sprint.html', ctx, context_instance=RequestContext(request))
    ctx = {'sprint': sprint}
    return render_to_response('sprint/eliminar_sprint.html', ctx, context_instance=RequestContext(request))


#----------------------------------------------------------------------------------------------------------------
def consultar_sprint_view(request, id_sprint):
    c_form = consultar_sprint_form()
    if request.method == 'GET':
        s = sprint.objects.get(pk=id_sprint)
        c_form = consultar_sprint_form(initial={
                                        'id':s.id_sprint,
                                         'nombre':s.nombre,
                                         'fecha_creacion':s.fecha_creacion,
                                         'fecha_inicio':s.fecha_inicio,
                                         'fecha_fin':s.fecha_fin,
                                         'release_asociado':s.release_asociado,
					 'flujo_asociado':s.flujo_asociado,
                                         })
    ctx = {'form':c_form}
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
            print busqueda
            if busqueda == 'nombre':
                s = sprint.objects.filter(nombre=parametro)
                ctx = {'mensaje': 'Sprints con nombre %s' % (parametro), 'sprints':s, 'b_form':b_form2}
                return render_to_response('sprint/adm_sprint.html', ctx, context_instance=RequestContext(request))
            elif busqueda == 'fecha_creacion':
                s = sprint.objects.filter(fecha_creacion=parametro)
                ctx = {'mensaje': 'Sprints con fecha de creacion %s' % (parametro), 'sprints':s, 'b_form':b_form2}
                return render_to_response('sprint/adm_sprint.html', ctx, context_instance=RequestContext(request))
#            else :
#                s = sprint.objects.filter(username=parametro)
#                ctx = {'mensaje': 'Usuario %s' %(parametro),'users':u,'form':form2}
#                return render_to_response('usuario/adm_usuario.html', ctx, context_instance=RequestContext(request))
    ctx = {'b_form': b_form}
    return render_to_response('sprint/buscar_sprint.html', ctx, context_instance=RequestContext(request))

