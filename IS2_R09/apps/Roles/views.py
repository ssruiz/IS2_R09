from django.shortcuts import render, render_to_response
from IS2_R09.apps.Roles.forms import group_form,consultar_rol_form,buscar_rol_form
from django.template.context import RequestContext
from django.contrib.auth.models import Group,Permission
import datetime
from django.http.response import HttpResponseRedirect
from django.contrib.auth import backends

# Create your views here.


def adm_rol_view(request):
    roles = Group.objects.all()
    form2 = buscar_rol_form()
    ctx = {'roles': roles,'form':form2}
    return render_to_response('roles/adm_roles.html',ctx,context_instance= RequestContext(request))

def crear_rol_view(request):
    form = group_form()
    now = datetime.datetime.now().date()
    print now
    if request.method == 'POST':
        form = group_form(request.POST)
        if form.is_valid():
            rol= form.save()
            roles = Group.objects.all()
            ctx = {'roles': roles,'mensaje':'Rol Creado','icono':'icon-yes.gif','form':buscar_rol_form()}
            return HttpResponseRedirect('/adm_rol/',ctx)
    return render_to_response('roles/crear_rol.html',{'form':form},context_instance= RequestContext(request))


def modificar_rol_view(request,id_rol):
    rol= Group.objects.get(id=id_rol)
  #  permisos = rol.get_group_permissions()
    
    rol_form= group_form()    
    if request.method == 'POST':
        rol_form= group_form(request.POST,instance=rol)
        if rol_form.is_valid():
            #formulario validado correctamente
            rol_form.save()
            ctx = {'roles': Group.objects.all(),'mensaje':'Rol Modificado','icono':'icon-yes.gif','form':buscar_rol_form()}
            return HttpResponseRedirect('/adm_rol/',ctx)
    if request.method == 'GET':
        rol_form= group_form(instance=rol)
        ctx = { 'rol_form': rol_form}
        return render_to_response('roles/modificar_rol.html', ctx, context_instance=RequestContext(request))

def eliminar_rol_view(request,id_rol):
    '''vista que controla la eliminacion de roles del sistema'''
    rol = Group.objects.get(id=id_rol)
    if request.method == 'POST':
        rol = rol.__class__.objects.get(id=id_rol)
        rol.delete()
        roles = Group.objects.all()
        ctx = {'mensaje': 'Rol Eliminado','roles':roles,'icono':'icon-yes.gif','form':buscar_rol_form()}
        return HttpResponseRedirect('/adm_rol/', ctx)
    ctx = {'rol': rol}
    return render_to_response('roles/eliminar_rol.html', ctx, context_instance=RequestContext(request))
#--------------------------------------------------------------------------------------------------------
def consultar_rol_view(request,id_rol):
    form= consultar_rol_form()
    if request.method == 'GET':
        r = Group.objects.get(pk=id_rol)
        form= consultar_rol_form(instance=r)
        ctx = {'form':form}
        return render_to_response('roles/consultar_rol.html', ctx, context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('roles/consultar_rol.html', ctx, context_instance=RequestContext(request))
#-------------------------------------------------------------------------------------------------------

def buscar_rol_view(request):
    form = buscar_rol_form()
    if(request.method=='POST'):
        form = buscar_rol_form(request.POST)
        form2 = buscar_rol_form()
        if form.is_valid():
            busqueda= form.cleaned_data['opciones']
            parametro = form.cleaned_data['busqueda']
            if busqueda== 'nombre':
                u = Group.objects.filter(name=parametro)
                if u :
                    ctx = {'mensaje': 'Rol con nombre %s' %(parametro),'roles':u,'form':form2}
                    return render_to_response('roles/adm_roles.html', ctx, context_instance=RequestContext(request))
                u = Group.objects.all()
                ctx = {'mensaje': 'Ningun rol %s encontrado' %(parametro),'roles':u,'form':form2,'icono':'icon_alert.gif'}
                return render_to_response('roles/adm_roles.html', ctx, context_instance=RequestContext(request))    
    ctx = {'form': form}
    return render_to_response('roles/buscar_rol.html', ctx, context_instance=RequestContext(request))
