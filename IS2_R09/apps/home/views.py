from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from IS2_R09.apps.home.forms import login_form
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
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