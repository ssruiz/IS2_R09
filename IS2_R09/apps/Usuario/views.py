# -*- encoding: utf-8 -*-
"""
    Vistas (Views)
    ==============
    
    Módulo que contiene las vistas del módulo L{Home<IS2_R09.apps.Usuario>}, encargadas de controlar las
    distintas operaciones aplicables al mismo.
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from IS2_R09.apps.Usuario.forms import crear_usuario_form,usuario_form,extension_usuario_form,\
    consultar_usuario_form, buscar_usuario_form
from IS2_R09.apps.Usuario.models import usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
from django.http.response import HttpResponseRedirect
from IS2_R09.apps.Notificaciones.views import notificar,notificar_creacion_usuario,\
    notificar_mod_usuario, notificar_elim_usuario
# Create your views here.

@login_required(login_url= URL_LOGIN)
def adm_usuario_view(request):
    """
        Administrar Usuario.
        ====================
        
        Vista que controla la interfaz de administración de usuarios.
    """
    users = User.objects.all()
    form = buscar_usuario_form()
    ctx={'usuario':request.user,'users':users,'form':form}
    return render_to_response('usuario/adm_usuario.html',ctx,context_instance=RequestContext(request))

# vista que controla la creacion de usuarios
@login_required(login_url= URL_LOGIN)
def crear_usuario_view(request):
    form = crear_usuario_form()
    if request.method == "POST":
        form = crear_usuario_form(request.POST) # se obtiene los datos del formulario
        if form.is_valid():
            usuario = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email =form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(username=usuario, email=email,password= password_one,first_name=nombre,last_name=apellido)
            u.save()
            notificar_creacion_usuario(u)
            return render_to_response('usuario/adm_usuario.html', {'mensaje': 'Usuario Creado.','users':User.objects.all(),'icono':'icon-yes.gif','form': buscar_usuario_form()},context_instance=RequestContext(request))
        else:
            ctx = {'form':form}
            return render_to_response('usuario/crear_usuario.html',ctx,context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('usuario/crear_usuario.html',ctx,context_instance=RequestContext(request))

# esta vista devuelve la interfaz de amdnisitracion de sesion
@login_required(login_url=URL_LOGIN)
def adm_sesion_view(request):
    return render_to_response('usuario/adm_sesion.html',{'usuario':request.user},context_instance=RequestContext(request))

# vista que controla la modificacion de datos del usuario que inicio sesion
@login_required(login_url=URL_LOGIN)
def mod_datos_view(request):
    user_form= usuario_form()
    exten_form=extension_usuario_form()
    if request.method == 'POST':
        # formulario enviado
        if request.FILES:
            user_form = usuario_form(request.POST,instance=request.user)
            perfil_form = extension_usuario_form(request.POST,request.FILES,request.user.usuario)
        #print user_form.username
            if user_form.is_valid() and perfil_form.is_valid():
            # formulario validado correctamente
                actual = request.user.usuario
                actual.telefono = request.POST['telefono']
                actual.foto = request.FILES['foto']
                actual.save()
                i=user_form.save()
                #notificar_mod_usuario(request.user)
                return HttpResponseRedirect('/')
        else:
            user_form = usuario_form(request.POST,instance=request.user)
            if user_form.is_valid():
            #formulario validado correctamente
                actual = request.user.usuario
                actual.telefono = request.POST['telefono']
               # actual.foto = request.FILES['foto']
                actual.save()
                i=user_form.save()
                #notificar_mod_usuario(request.user)
                return HttpResponseRedirect('/')
    else:
        user_form = usuario_form (instance=request.user)
        exten_form = extension_usuario_form(instance=request.user.usuario)
        return render_to_response('usuario/mod_datos.html', { 'user_form': user_form,  'exten_form': exten_form }, context_instance=RequestContext(request))
    return render_to_response('usuario/mod_datos.html', { 'user_form': user_form,  'exten_form': exten_form }, context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def modificar_usuario_view(request,id_usuario):
    u= User.objects.get(id=id_usuario)
    user_form= usuario_form()
    exten_form=extension_usuario_form()    
    if request.method == 'POST':
        if request.FILES:
            user_form = usuario_form(request.POST,instance=u)
            perfil_form = extension_usuario_form(request.POST,request.FILES,instance=u.usuario)
        #print user_form.username
            if user_form.is_valid() and perfil_form.is_valid():
            # formulario validado correctamente
                actual = u.usuario
                actual.telefono = request.POST['telefono']
                actual.foto = request.FILES['foto']
                actual.save()
                i=user_form.save()
                notificar_mod_usuario(u)
                return render_to_response('usuario/adm_usuario.html', {'mensaje': 'Usuario modificado.','users':User.objects.all(),'icono':'icon-yes.gif','form': buscar_usuario_form()},context_instance=RequestContext(request))
        else:
            user_form = usuario_form(request.POST,instance=u)
            if user_form.is_valid():
            #formulario validado correctamente
                actual = u.usuario
                actual.telefono = request.POST['telefono']
               # actual.foto = request.FILES['foto']
                actual.save()
                i=user_form.save()
                notificar_mod_usuario(u)
                return render_to_response('usuario/adm_usuario.html', {'mensaje': 'Usuario modificado.','users':User.objects.filter(is_active=True),'icono':'icon-yes.gif','form': buscar_usuario_form()},context_instance=RequestContext(request))
    if request.method == 'GET':
        user_form= usuario_form(initial={
                                         'username':u.username,
                                         'first_name':u.first_name,
                                         'last_name':u.last_name,
                                         'email':u.email,
                                         })
        foto = None
        if u.usuario.foto != '':
            foto=u.usuario.foto.url
        exten_form=extension_usuario_form(instance=u.usuario)
        ctx = { 'user_form': user_form,  'exten_form': exten_form ,'foto':foto}
        return render_to_response('usuario/modificar_usuario.html', ctx, context_instance=RequestContext(request))
    return render_to_response('usuario/modificar_usuario.html', { 'user_form': user_form,  'exten_form': exten_form }, context_instance=RequestContext(request))

#-----------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def eliminar_usuario_view(request,id_usuario):
    '''vista que controla la eliminacion de usuarios del sistema'''
    user = User.objects.get(pk=id_usuario)
    if request.method == 'POST':
        user = User.objects.get(pk=id_usuario)
        mail = user.email
        user.delete()
        notificar_elim_usuario(mail)
        users = User.objects.all()
        ctx = {'mensaje': 'Usuario eliminado','users':users,'form': buscar_usuario_form()}
        return render_to_response('usuario/adm_usuario.html', ctx, context_instance=RequestContext(request))
    ctx = {'usuario': user}
    return render_to_response('usuario/eliminar_usuario.html', ctx, context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def buscar_usuario_view(request):
    form = buscar_usuario_form()
    if(request.method=='POST'):
        form = buscar_usuario_form(request.POST,request.FILES)
        form2 = buscar_usuario_form()
        if form.is_valid():
            busqueda= form.cleaned_data['opciones']
            parametro = form.cleaned_data['busqueda']
            if busqueda== 'nombre':
                u = User.objects.filter(first_name=parametro)
                ctx = {'mensaje': 'Usuarios con nombre %s' %(parametro),'users':u,'form':form2}
                return render_to_response('usuario/adm_usuario.html', ctx, context_instance=RequestContext(request))
            elif busqueda== 'apellido':
                u = User.objects.filter(last_name=parametro)
                ctx = {'mensaje': 'Usuarios con apellido %s' %(parametro),'users':u,'form':form2}
                return render_to_response('usuario/adm_usuario.html', ctx, context_instance=RequestContext(request))
            else :
                u = User.objects.filter(username=parametro)
                ctx = {'mensaje': 'Usuario %s' %(parametro),'users':u,'form':form2}
                return render_to_response('usuario/adm_usuario.html', ctx, context_instance=RequestContext(request))
    ctx = {'form': form}
    return render_to_response('usuario/buscar_usuario.html', ctx, context_instance=RequestContext(request))

#------------------------------------------------------------------------------------------------
@login_required(login_url= URL_LOGIN)
def consultar_usuario_view(request,id_usuario):
    form= consultar_usuario_form()
    if request.method == 'GET':
        u = User.objects.get(pk=id_usuario)
        form= consultar_usuario_form(initial={
                                        'id':u.id,
                                         'username':u.username,
                                         'first_name':u.first_name,
                                         'last_name':u.last_name,
                                         'email':u.email,
                                         'telefono':u.usuario.telefono,
                                         })
        foto = None
        if u.usuario.foto != '':
            foto=u.usuario.foto.url
            print 'a'
        ctx = {'form':form,'foto': foto}
        return render_to_response('usuario/consultar_usuario.html', ctx, context_instance=RequestContext(request))
    