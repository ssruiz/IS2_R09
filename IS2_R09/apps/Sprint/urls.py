'''
Created on 23/4/2015

@author: meliam
'''
from django.conf.urls import patterns,url

urlpatterns = patterns('IS2_R09.apps.Sprint.views',
    url(r'^adm_sprint/$','adm_sprint_view', name= 'vista_adm_sprint'),
    url(r'^crear_sprint/$','crear_sprint_view', name= 'vista_crear_sprint'),
    url(r'^modificar/sprint/(?P<id_sprint>.*)/$','modificar_sprint_view', name= 'vista_mod_sprint'),
    url(r'^eliminar/sprint/(?P<id_sprint>.*)/$','eliminar_sprint_view', name= 'vista_eliminar_sprint'),
    url(r'^consultar/sprint/(?P<id_sprint>.*)/$','consultar_sprint_view', name= 'vista_consultar_sprint'),
    url(r'^buscar_sprint/$','buscar_sprint_view', name= 'vista_buscar_sprint'),
    
)