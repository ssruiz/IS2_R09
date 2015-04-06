from django.shortcuts import render, render_to_response
from IS2_R09.apps.Proyecto.forms import proyecto_form, equipo_form,\
    cantidad_form
from IS2_R09.apps.Proyecto.models import proyecto,Equipo
from django.template.context import RequestContext
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
# Create your views here.

def adm_proyecto_view(request):
    ''''Vista que controla la interfaz de administracion de proyectos'''
    proyectos= proyecto()
    if request.user.is_staff:
        '''Si el usuario es administrador se le listan todos los proyectos'''
        proyectos = proyecto.objects.all()
        ctx={'proyectos':proyectos}
        return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
    ''''En caso contrario se le lista solo los proyectos al que esta asignado'''
    proyectos = proyecto.objects.filter(miembro=request.user)
    ctx={'proyectos':proyectos}
    return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def crear_proyecto_view(request):
    '''Vista que controla creacion de Proyectos'''
    form= proyecto_form()
    if request.method == 'POST':
        form = proyecto_form(request.POST)
        if form.is_valid():
            form.save()
            ctx={}
            return render_to_response('proyecto/adm_proyecto.html',ctx,context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('proyecto/crear_proyecto.html',ctx,context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------------------------------------------------


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
            return render_to_response('proyecto/adm_proyecto.html',context_instance=RequestContext(request))
    
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
            formset= equipo_formset(initial=[{'proyect':p,}],queryset=Equipo.objects.none())
            ctx = {'form':formset,'p':p.id}
            return render_to_response('proyecto/asignar_equipo.html',ctx,context_instance=RequestContext(request))
        
    ctx = {'form':formset}
    return render_to_response('proyecto/asignar_equipo.html',ctx,context_instance=RequestContext(request))