#!/usr/bin/python
# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from keyring.backend import json
from IS2_R09.apps.US.models import us
from IS2_R09.apps.Sprint.models import sprint
from IS2_R09.apps.Release.models import release
from IS2_R09.apps.Proyecto.models import proyecto, Equipo
from django.contrib.auth.decorators import login_required
from IS2_R09.settings import URL_LOGIN
import datetime

# Create your views here.
@login_required(login_url= URL_LOGIN)
def sacar_release_view(request):
    if request.is_ajax():
        i = request.GET['k'] # kanban
        ust = us.objects.get(id=i)
        sprint_a = sprint.objects.get(id=ust.sprint_asociado.id)
        proyecto_us= ust.proyecto_asociado
        proyect = proyecto.objects.get(id=proyecto_us.id)
        # El usuario debe estar asignado al user story y ser scrum master o administrador
        if not us.objects.filter(id=i,usuario_asignado=request.user).exists():
            if Equipo.objects.filter(proyect=proyect,miembro=request.user).exists():
                e = Equipo.objects.get(proyect=proyect,miembro=request.user)
                if not e.rol.name == 'Scrum':
                    l = {'lanzar': 'no','mensaje':'No posee permisos de Scrum master para finalizar este User Story.'}
                    return HttpResponse(json.dumps(l))
            elif not request.user.is_staff:
                l = {'lanzar': 'no','mensaje':'No posee permisos para aprobar User Story.'}
                return HttpResponse(json.dumps(l))
        
        else:
            e = Equipo.objects.get(proyect=proyect,miembro=request.user)
            if not e.rol.name == 'Scrum':
                l = {'lanzar': 'no','mensaje':'No posee permisos de Scrum master para finalizar este User Story.'}
                return HttpResponse(json.dumps(l))
            elif not request.user.is_staff:
                l = {'lanzar': 'no','mensaje':'No posee permisos para aprobar User Story.'}
                return HttpResponse(json.dumps(l))
            
        if release.objects.filter(sprint_asociado=sprint_a,lanzado='no').exists():
            release_actual = release.objects.get(sprint_asociado=sprint_a,lanzado='no')
            ust.release_asociado = release_actual
            ust.save()
        else:
            release_actual = release.objects.create(nombre='Release Sprint: %s' %(sprint_a.nombre),sprint_asociado=sprint_a,proyecto_asociado=ust.proyecto_asociado)
            ust.release_asociado = release_actual
            ust.save()
        print ust.nombre
        l = {'lanzar':'si','us': ust.nombre,'mensaje':'No esta asignado a este User Story.'}
        return HttpResponse(json.dumps(l))

@login_required(login_url= URL_LOGIN)
def lanzar_release_view(request):
    if request.is_ajax():
        
        i = request.GET['k'] # proyecto
        proyect = proyecto.objects.get(id=i)
        print proyect
        
        # El usuario debe estar asignado al user story, ser scrum master o administrador
        if Equipo.objects.filter(proyect=proyect,miembro=request.user).exists():
            e = Equipo.objects.get(proyect=proyect,miembro=request.user)
            if not e.rol.name == 'Scrum' or not request.user.is_staff:
                l = {'lanzar': 'no','mensaje':'No posee permisos de Scrum master para sacar un Release.'}
                return HttpResponse(json.dumps(l))
        elif not request.user.is_staff:
            l = {'lanzar': 'no','mensaje':'No posee permisos para aprobar User Story.'}
            return HttpResponse(json.dumps(l))
        
        if proyect.sprint_actual == '':
            l = {'mensaje':'Ningun sprint en desarrollo. Consulte en administracion de proyectos.'}
            return HttpResponse(json.dumps(l))
        else:
            sprint_actual= sprint.objects.get(id=proyect.sprint_actual)
            sin_aprobar = us.objects.filter(sprint_asociado=sprint_actual,release_asociado__lanzado='no').count()
            sin_release = us.objects.filter(sprint_asociado=sprint_actual,release_asociado=None).count()
            print sin_release
            if sin_release == 0:
                proyect.sprint_actual= ''
                sprint_actual.finalizado='si'
                sprint_actual.save()
                proyect.save()
                l = {'mensaje':'Release sacado! Ademas Sprint Finalizado. Recargue la pagina'}
                return HttpResponse(json.dumps(l))
        
            if not release.objects.filter(sprint_asociado=sprint_actual,lanzado='no').exists():
                l = {'mensaje':'Ningun User Story actualmente aprobado para Release.'}
                return HttpResponse(json.dumps(l))
            release_actual = release.objects.get(sprint_asociado=sprint_actual,lanzado='no')
            release_actual.lanzado='si'
            release_actual.fecha_lanzamiento = datetime.date.today() 
            release_actual.save()
        
            l = {'mensaje':'Release sacado! Consulte en administracion de proyectos.'}
            return HttpResponse(json.dumps(l))