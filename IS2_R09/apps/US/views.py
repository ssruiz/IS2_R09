from django.shortcuts import render_to_response
from IS2_R09.apps.US.models import us
from IS2_R09.apps.US.forms import us_form,buscar_us_form, modificar_form,consultar_form
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
@login_required(login_url= URL_LOGIN)
def eliminar_us_view(request,id_us):
    '''vista que controla la eliminacion de usuarios del sistema'''
    ust = us.objects.get(pk=id_us)
    if request.method == 'POST':
        ust.delete()
        if request.user.is_staff:
                usst = us.objects.all()
                ctx={'us':usst,'mensaje':'us Eliminado','form':buscar_us_form()}
                return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
        else:
            usst = us.objects.filter(miembro=request.user)
            ctx={'us':usst,'mensaje':'us Eliminado','form':buscar_us_form()}
            return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
    
    ctx = {'US': ust}
    return render_to_response('US/eliminar_us.html', ctx, context_instance=RequestContext(request))
#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def buscar_us_view(request):
    form = buscar_us_form()
    if(request.method=='POST'):
        form = buscar_us_form(request.POST)
        form2 = buscar_us_form()
        if form.is_valid():
            busqueda= form.cleaned_data['opciones']
            parametro = form.cleaned_data['busqueda']
            if busqueda== 'nombre':
                p = us.objects.filter(nombre=parametro)
                ctx = {'mensaje': 'uss con nombre %s' %(parametro),'ussk':p,'form':form2}
                return render_to_response('US/adm_us.html', ctx, context_instance=RequestContext(request))
            elif busqueda== 'cliente':
                try:
                    u = User.objects.get(username=parametro)
                    p = us.objects.filter(cliente=u)
                    ctx = {'mensaje': 'uss con cliente %s' %(u),'ussk':p,'form':form2}
                    return render_to_response('US/adm_us.html', ctx, context_instance=RequestContext(request))
                except:
                        if request.user.is_staff:
                            ust = us.objects.all()
                            ctx={'ussk':ust,'mensaje':'Cliente con username %s no existe'%(parametro),'form':buscar_us_form()}
                            return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
                        else:
                            ust = us.objects.filter(miembro=request.user)
                            ctx={'ussk':ust,'mensaje':'Cliente con username %s no existe'%(parametro),'form':buscar_us_form()}
                            return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
                    
    ctx = {'form': form}
    return render_to_response('US/adm_us.html', ctx, context_instance=RequestContext(request))


@login_required(login_url= URL_LOGIN)
def modificar_us_view(request,id_us):
    if request.method == 'POST':
        ust = us.objects.get(id=id_us)
        form = modificar_form(request.POST,instance=ust)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                ussk = ust.objects.all()
                ctx={'uss':ussk,'mensaje':'us modificado','form':buscar_us_form()}
                return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
            else:
                ussk = us.objects.filter(miembro=request.user)
                ctx={'uss':ussk,'mensaje':'us Modificado','form':buscar_us_form()}
                return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
    
    if request.method=='GET':
        ust = us.objects.get(id=id_us)
        form = modificar_form(instance= ust)
        ctx = {'form':form}
        return render_to_response('US/modificar_us.html',ctx,context_instance=RequestContext(request))
    proyect = us.objects.get(id=id_us)
    form = modificar_form(instance= proyect)
    ctx = {'form':form}
    return render_to_response('US/modificar_us.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def consultar_us_view(request,id_us):
    if request.method=='GET':
        ust = us.objects.get(id=id_us)
        form = consultar_form(instance= ust)
        form.fields['flujos'].queryset=ust.flujos.all()
        ctx = {'form':form}
        return render_to_response('US/consultar_us.html',ctx,context_instance=RequestContext(request))

3