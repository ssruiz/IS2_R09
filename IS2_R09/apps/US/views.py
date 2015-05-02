# -*- encoding: utf-8 -*-

"""
    Modulo que controla las operaciones sobre los B{User Stories} de los clientes.  
    @author: Samuel Ruiz,Melissa Bogado,Rafael Ricardo
"""
from IS2_R09.apps.Notificaciones.views import notificar_asignacion_us,\
    notificar_eli_proyecto, notificar_eli_us
__docformat__ = "Epytext"  

from django.shortcuts import render_to_response
from IS2_R09.apps.US.models import us
from IS2_R09.apps.US.forms import us_form,buscar_us_form, modificar_form,consultar_form

from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from IS2_R09.settings import URL_LOGIN
from IS2_R09.apps.Proyecto.models import Equipo, proyecto
from django.contrib.auth.models import User,Group
from IS2_R09.apps.Flujo.forms import kanban_form
from IS2_R09.apps.Flujo.models import flujo,kanban
@login_required(login_url= URL_LOGIN)
def adm_us_view(request):
    """
        adm_us_view(request)
        Vista que controla la interfaz de administración de B{User Story}
        @param request: Almacena la información del usuario en sesión que ingresa a la interfaz
        de administración de B{User Story}.
        @requires: Estar logeado dentro del sistema.
    """
    ust= us()
    if request.user.is_staff:
        """Si el usuario es administrador se le listan todos los User Story """
        ust = us.objects.all().order_by('prioridad')
        ctx={'uss':ust,'form':buscar_us_form()}
        return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
    """En caso contrario se le lista solo los User Stories al que esta asignado"""
    ust = us.objects.filter(usuario_asignado=request.user).order_by('prioridad')
    ctx={'uss':ust,'form':buscar_us_form()}
    return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def crear_us_view(request):
    """
        crear_us_view(request)
        Vista que controla la modificación de un B{User Story}.
        @param request: Almacena la información del usuario que desea crear un B{User Story}.
        @requires: El usuario logeado debe tener rol de administrador o Scrum Master dentro del Proyecto 
        donde creará el B{User Story} 
    """
    form= us_form()
    if request.method == 'POST':
        form = us_form(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                """Si el usuario es administrador se le listan todos los User Stories"""
                ust = us.objects.all().order_by('prioridad')
                ctx={'uss':ust,'form':buscar_us_form()}
                return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
            else:
                """En caso contrario se le lista solo los user stories que tiene asignado"""
                ust = us.objects.filter(usuario_asignado=request.user).order_by('prioridad')
                ctx={'uss':ust,'form':buscar_us_form()}
                return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
    equipo = Equipo.objects.filter(miembro=request.user.id)
    role = Group.objects.get(name='Scrum')
    if Equipo.objects.filter(miembro=request.user.id, rol=role).exists():
        print request.user
    #form.fields['usuario_asignado'].queryset= proyecto.objects.filter(id__in=form['proyecto_asociado'].value()).equipo   
    ctx = {'form':form}
    return render_to_response('US/crear_us.html',ctx,context_instance=RequestContext(request))

#------------------------------------
@login_required(login_url= URL_LOGIN)
def modificar_us_view(request,id_us):
    """
        modificar_us_view(request,id_us)
        Vista que controla la modificación de un B{User Story}.
        @param request: Almacena la información del usuario que desea modificar el B{User Story}. 
        @param id_us: Almacena la clave del B{User Story} a modificar.
        @requires: El usuario logeado debe tener rol de administrador , rol de Scrum Master dentro del Proyecto
        o tener asignado el B{User Story} que modificará.
    """
    k= kanban_form()
    if request.method == 'POST':
        user_story = us.objects.get(id=id_us)
        form = us_form(request.POST,instance=user_story)
        ua= user_story.usuario_asignado.all()
        if form.is_valid():
            try:
                kan = kanban.objects.get(us=user_story)
                k = kanban_form(request.POST,instance=kan)
                if k.is_valid():
                    form.save()
                    kan.us=user_story
                    f=k.cleaned_data['fluj']
                    fj = flujo.objects.get(id=f.id)
                    act = fj.actividades.all()[:1].get()
                    kan.actividad = act
                    kan.fluj=f
                    kan.estado= 'td'
                    notificar_asignacion_us(ua,user_story.nombre)
                    kan.save()
                #kan.fluj= k.cleaned_data['fluj']
                #kan.save()
                    if request.user.is_staff:
                        '''Si el usuario es administrador se le listan todos los us'''
                        ust = us.objects.all().order_by('prioridad')
                        ctx={'uss':ust,'form':buscar_us_form()}
                        return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
            
                    else:
                        ust = us.objects.filter(usuario_asignado=request.user).order_by('prioridad')
                        ctx={'uss':ust,'form':buscar_us_form()}
                        return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
            except:
                k = kanban_form(request.POST)
                if k.is_valid():
                    f = k.cleaned_data['fluj']
                    fj = flujo.objects.get(id=f.id)
                    act = fj.actividades.all()[:1].get()
                    kan = kanban.objects.create(us=user_story,fluj=k.cleaned_data['fluj'],actividad=act)
                    notificar_asignacion_us(ua,user_story.nombre)
                    form.save()
                    #k.save()
                #kan.fluj= k.cleaned_data['fluj']
                #kan.save()
                    if request.user.is_staff:
                        '''Si el usuario es administrador se le listan todos los us'''
                        ust = us.objects.all().order_by('prioridad')
                        ctx={'uss':ust,'form':buscar_us_form()}
                        return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
            
                    else:
                        ust = us.objects.filter(usuario_asignado=request.user).order_by('prioridad')
                        ctx={'uss':ust,'form':buscar_us_form()}
                        return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
                
    if request.method=='GET':
        try:
            user_story = us.objects.get(id=id_us)
            kan = kanban.objects.get(us=user_story)
            
            p= proyecto.objects.get(id=user_story.proyecto_asociado.id)
            form =us_form(instance= user_story)
            form.fields['usuario_asignado'].queryset= p.miembro.all()
            #k.fields['us'].queryset = us.objects.get(id=id_us)
            
            #form.fields['flujo_asignado'].queryset= p.flujos.all()
            k =kanban_form(instance=kan)
            k.fields['fluj'].queryset = kan.fluj.all()
            ctx = {'form':form,'k':k}
            return render_to_response('US/modificar_us.html',ctx,context_instance=RequestContext(request))
        except:
            user_story = us.objects.get(id=id_us)
            p= proyecto.objects.get(id=user_story.proyecto_asociado.id)
            form =us_form(instance= user_story)
            form.fields['usuario_asignado'].queryset= p.miembro.all()
            #k.fields['us'].queryset = us.objects.get(id=id_us)
            k.fields['fluj'].queryset = p.flujos.all()
            #form.fields['flujo_asignado'].queryset= p.flujos.all()
            ctx = {'form':form,'k':k}
            return render_to_response('US/modificar_us.html',ctx,context_instance=RequestContext(request))
#---------------------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def eliminar_us_view(request,id_us):
    """
        eliminar_us_view(request,id_us)
        Vista que controla la eliminación de un B{User Story}.
        @param request: Almacena la información del usuario que desea eliminar el B{User Story}. 
        @param id_us: Almacena la clave del B{User Story} a eliminar.
        @requires: El usuario logeado debe tener rol de administrador o Scrum Master dentro del Proyecto 
        del que eliminará el B{User Story}
    """
    user_story = us.objects.get(pk=id_us)
    if request.method == 'POST':
        ua= user_story.usuario_asignado.all()
        nombre=user_story.nombre
        notificar_eli_us(ua,nombre)
        user_story.delete()
        
        if request.user.is_staff:
                '''Si el usuario es administrador se le listan todos los us'''
                ust = us.objects.all().order_by('prioridad')
                ctx={'uss':ust,'form':buscar_us_form()}
                return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
    
        else:
            ust = us.objects.filter(usuario_asignado=request.user).order_by('prioridad')
            ctx={'uss':ust,'form':buscar_us_form()}
            return render_to_response('US/adm_us.html',ctx,context_instance=RequestContext(request))
    
    ctx = {'user_story': user_story}
    return render_to_response('US/eliminar_us.html', ctx, context_instance=RequestContext(request))

#-------------------------------------------------------------------------------------------------------

@login_required(login_url= URL_LOGIN)
def consultar_us_view(request,id_us):
    """
        consultar_us_view(request,id_us)
        Vista que controla la consulta de información de un B{User Story}.
        @param request: Almacena la información del usuario que desea consultar datos del B{User Story}. 
        @param id_us: Almacena la clave del B{User Story} a consultar.
        @requires: El usuario debe estar logeado. 
    """
    if request.method=='GET':
        try:
            user_story = us.objects.get(id=id_us)
            kan = kanban.objects.get(us=user_story)
            print 'aaa'
            p= proyecto.objects.get(id=user_story.proyecto_asociado.id)
            
            form =consultar_form(instance= user_story)
            form.fields['usuario_asignado'].queryset= user_story.usuario_asignado.all()
            
            #k.fields['us'].queryset = us.objects.get(id=id_us)
            form.fields['proyecto_asociado'].queryset= proyecto.objects.filter(id=user_story.proyecto_asociado.id)
            #form.fields['flujo_asignado'].queryset= p.flujos.all()
            k =kanban_form(instance=kan)
            fluj= kan.fluj
            print fluj
            #k.fields['fluj'].queryset = kan.fluj.all()
            print 'bbb'
            ctx = {'form':form,'k':fluj,'p':p}
            
            return render_to_response('US/consultar_us.html',ctx,context_instance=RequestContext(request))
        except:
            user_story = us.objects.get(id=id_us)
            p= proyecto.objects.get(id=user_story.proyecto_asociado.id)
            form =consultar_form(instance= user_story)
            form.fields['usuario_asignado'].queryset= user_story.usuario_asignado.all()
            #form.fields['flujo_asignado'].queryset= p.flujos.all()
            form.fields['proyecto_asociado'].queryset= proyecto.objects.filter(id=user_story.proyecto_asociado.id)
            ctx = {'form':form,'p':p}
            return render_to_response('US/consultar_us.html',ctx,context_instance=RequestContext(request))


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
                ctx = {'mensaje': 'uss con nombre %s' %(parametro),'uss':p,'form':form2}
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