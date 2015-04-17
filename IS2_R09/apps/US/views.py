from django.shortcuts import render, render_to_response
from IS2_R09.apps.US.models import us
from IS2_R09.apps.US.forms import us_form,buscar_us_form
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
# Create your views here.
def adm_us_view(request):
    ''''Vista que controla la interfaz de administracion de us'''
    ust= us()
    if request.user.is_staff:
        '''Si el usuario es administrador se le listan todos los proyectos'''
        ust = us.objects.all()
        ctx={'uss':ust,'form':buscar_us_form()}
        
        return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
    ''''En caso contrario se le lista solo los user story al que esta asignado'''
    ust = us.objects.filter(usuario_asignado=request.user)
    ctx={'uss':ust,'form':buscar_us_form()}
    return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def crear_us_view(request):
    '''Vista que controla creacion de Proyectos'''
    form= us_form()
    if request.method == 'POST':
        form = us_form(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                '''Si el usuario es administrador se le listan todos los proyectos'''
                ust = us.objects.all()
                ctx={'uss':ust,'form':buscar_us_form()}
                return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
            else:
                ''''En caso contrario se le lista solo los user story al que esta asignado'''
                ust = us.objects.filter(usuario_asignado=request.user)
                ctx={'uss':ust,'form':buscar_us_form()}
                return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))        
    ctx = {'form':form}
    return render_to_response('US/crear_us.html',ctx,context_instance=RequestContext(request))

#------------------------------------