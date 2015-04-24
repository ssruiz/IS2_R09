"""
    Admin de Django
    ===============
    
    Modulo que registra los L{modelos<IS2_R09.apps.Flujo.models>}, creados para los B{Flujos},
    en el Admin de Django  
""" 
from django.contrib import admin
from IS2_R09.apps.Flujo.models import flujo,actividad
# Register your models here.
admin.site.register(flujo)
admin.site.register(actividad)