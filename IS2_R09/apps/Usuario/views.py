from django.shortcuts import render_to_response
from django.template import RequestContext
from IS2_R09.apps.Usuario.forms import crear_usuario_form,usuario_form,extension_usuario_form,\
    manage_usuario_form
from IS2_R09.apps.Usuario.models import usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
from django.http.response import HttpResponseRedirect

# Create your views here.

@login_required(login_url= URL_LOGIN)
def adm_usuario_view(request):
    users = User.objects.all()
    ctx={'usuario':request.user,'users':users}
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
            return HttpResponseRedirect('/adm_usuario/')
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
    user_form= usuario_form(prefix="user",instance=request.user)
    exten_form=extension_usuario_form(prefix="usuario",instance=request.user.usuario)
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
                return render_to_response('usuario/adm_usuario.html', {'mensaje': 'Usuario modificado.','users':User.objects.all()},context_instance=RequestContext(request))
        else:
            user_form = usuario_form(request.POST,instance=u)
            if user_form.is_valid():
            #formulario validado correctamente
                actual = u.usuario
                actual.telefono = request.POST['telefono']
               # actual.foto = request.FILES['foto']
                actual.save()
                i=user_form.save()
                return render_to_response('usuario/adm_usuario.html', {'mensaje': 'Usuario modificado.','users':User.objects.filter(is_active=True)},context_instance=RequestContext(request))
    if request.method == 'GET':
        user_form= usuario_form(initial={
                                         'username':u.username,
                                         'first_name':u.first_name,
                                         'last_name':u.last_name,
                                         'email':u.email,
                                         })
        exten_form=extension_usuario_form(initial={
                                         'telefono':u.usuario.telefono,
                                         'foto':u.usuario.foto,
                                         })
        ctx = { 'user_form': user_form,  'exten_form': exten_form ,'foto':u.usuario.foto}
        return render_to_response('usuario/modificar_usuario.html', ctx, context_instance=RequestContext(request))
    return render_to_response('usuario/modificar_usuario.html', { 'user_form': user_form,  'exten_form': exten_form }, context_instance=RequestContext(request))

#-----------------------------------------------------------------------------------------
def eliminar_usuario_view(request,id_usuario):
    user = User.objects.get(pk=id_usuario)
    ctx = {'usuario': user}
    return render_to_response('usuario/eliminar_usuario.html', ctx, context_instance=RequestContext(request))