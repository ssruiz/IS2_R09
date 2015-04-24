# -*- encoding: utf-8 -*-
"""
    Vistas (Views)
    ==============
    
    Módulo que contiene las vistas del módulo L{Home<IS2_R09.apps.home>}, encargadas de controlar las
    distintas operaciones aplicables al mismo.
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from IS2_R09.apps.home.forms import login_form, recuperar_contra
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
from django.contrib.auth.models import User
from django.core.mail import send_mail 
# Create your views here.


# vista inicial del sistema
@login_required(login_url= URL_LOGIN)
def index_view(request):
    """
        index_view(request)
        Index
        =====
        
        Vista inicial del sistema que administra la página que ve el usuario al logearse.
        @note: es utilizada solamente una vez, al logearse.
        @param request: Contiene información sobre la consulta realizada a la vista como
        el usuario que la hizo, desde dónde se hizo, datos que incluye la consulta(si existieran) etc.
    """
    return render_to_response('home/index.html',{'usuario':request.user},context_instance= RequestContext(request))

def menu_view(request):
    """
        menu_view(request)
        Menú
        ====
        
        Vista del sistema que administra la página que ve el usuario al acceder al menú.
        @param request: Contiene información sobre la consulta realizada a la vista como
        el usuario que la hizo, desde dónde se hizo, datos que incluye la consulta(si existieran) etc.
    """
    return render_to_response('home/menu.html',{'usuario':request.user},context_instance= RequestContext(request))

# vista del login
def login_view(request):
    """
        login_view(request)
        Login
        =====
        
        Vista inicial del sistema que administra la página que ve el usuario tratar de acceder al sistema.
        Se encarga de controlar si el usuario esta registrado en el sistema y en dicho caso permitirle el acceso.
        @param request: Contiene información sobre la consulta realizada a la vista como
        el usuario que la hizo, desde dónde se hizo, datos que incluye la consulta(si existieran) etc.
    """
    mensaje = ""
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = login_form(request.POST)
            if form.is_valid():
                next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                ctx = {'usuario':username}
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect(next)
                    #return HttpResponseRedirect('/')
                else:
                    mensaje = "Usuario y/o password incorrectos"
        next = request.REQUEST.get('next')
        form = login_form()
        ctx= {'form':form,'next':next,'mensaje':mensaje}
        return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    """
        logout_view(request)
        Logout
        ======
        
        Vista del sistema que administra el cierre de sesión del usuario logeado.
        @param request: Contiene información sobre la consulta realizada a la vista como
        el usuario que la hizo, desde dónde se hizo, datos que incluye la consulta(si existieran) etc.
    """
    logout(request)
    return HttpResponseRedirect('/login/')

def recuperar_pass_view(request):
    """
        recuperar_pass_view(request)
        Recuperar Contraseña
        ====================
        
        Vista del sistema que administra la recuperación de la contraseña de cierto usuario.
        
        Se solicita el email del usuario, se controla que el email este registrado en la base de datos
        y en dicho caso se genera una contraseña aleatoria y se le asigna al usuario notificandole vía
        mail los cambios y su nueva contraseña. 
        @param request: Contiene información sobre la consulta realizada a la vista como
        el usuario que la hizo, desde dónde se hizo, datos que incluye la consulta(si existieran) etc.
    """
    form = recuperar_contra()
    if request.method == "POST":
        form = recuperar_contra(request.POST)
        if form.is_valid():
            mail =form.cleaned_data['email']
            passw= User.objects.make_random_password()
            user = User.objects.get(email = mail)
            user.set_password(passw)
            user.save() 
            send_mail('Recuperacion de contrasenha', 'Usuario su nuevo password es %s.' %(passw), 'is2.pagiles@gmail.co',
    [mail], fail_silently=False)
            return HttpResponseRedirect('/login/')
        else:
            ctx = {'form':form}
            return render_to_response('home/passw_recovery.html',ctx,context_instance= RequestContext(request)) 
        
    ctx = {'form':form}
    return render_to_response('home/passw_recovery.html',ctx,context_instance= RequestContext(request))
                