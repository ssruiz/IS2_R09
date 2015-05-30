#!/usr/bin/python
# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from keyring.backend import json
from IS2_R09.apps.Charts.models import charts
from IS2_R09.apps.Proyecto.models import proyecto
from IS2_R09.apps.Sprint.models import sprint



# Create your views here.
def bd_load(request):
    i = request.GET['sp_id'] # kanban
    p = request.GET['p'] # kanban
    
    
    pr = proyecto.objects.get(id=int(p))
    sp = sprint.objects.get(id=int(i))
    tt= sp.tiempo_estimado
    dd = int(tt/24)
    puntos = charts.objects.filter(proyect=pr,sprint_actual=sp)
    
    v = []
    t = [[1,tt],[dd,0]]
    for c in puntos:
        v.append([c.ejex,c.ejey])
    l = {'trabajado':v,'estimado':t}
    return HttpResponse(json.dumps(l))
