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
def index_view(request):
    return render_to_response('home/index.html',{'usuario':request.user},context_instance= RequestContext(request))

def menu_view(request):
    return render_to_response('home/menu.html',{'usuario':request.user},context_instance= RequestContext(request))

# vista del login
def login_view(request):
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
        ctx= {'form':form,'next':next}
        return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def recuperar_pass_view(request):
    ''' view que maneja la recuperacion de contrasenha de un usuario.'''
    form = recuperar_contra()
    if request.method == "POST":
        form = recuperar_contra(request.POST)
        if form.is_valid():
            print "llegue"
            mail =form.cleaned_data['email']
            passw="ffds"
            print "llegue2"
            user = User.objects.get(email = mail)
            print user
            user.set_password(passw)
            user.save()
            send_mail('Recuperacion de contrasenha', 'Usuario su nuevo password es %s.' %(passw), 'is2.pagiles@gmail.co',
    ['samuel.sebastian.ruiz@gmail.com'], fail_silently=False)
            return HttpResponseRedirect('/')
        else:
            ctx = {'form':form}
            return render_to_response('home/passw_recovery.html',ctx,context_instance= RequestContext(request)) 
        
    ctx = {'form':form}
    return render_to_response('home/passw_recovery.html',ctx,context_instance= RequestContext(request))
                