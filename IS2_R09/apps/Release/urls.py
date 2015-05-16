"""
Created on 15/5/2015

@author: Melissa Bogado, Samuel Ruiz, Rafael Ricardo
"""
"""
    URLS
    ====
    
    Modulo que controla las urls de las L{Vistas<IS2_R09.apps.Release.views>} utilizadas en
    L{Release<IS2_R09.apps.Release>}.
"""
from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Release.views',
    url(r'^crear_release/$','crear_release_view', name= 'vista_crear_release'),
    url(r'^adm_release/$','adm_release_view', name= 'vista_adm_release'),
    url(r'^modificar/release/(?P<id_release>.*)/$','modificar_release_view', name= 'vista_modificar_release'),
    url(r'^eliminar/release/(?P<id_release>.*)/$','eliminar_release_view', name= 'vista_eliminar_release'),
    url(r'^consultar/release/(?P<id_release>.*)/$','consultar_release_view', name= 'vista_consultar_release'),
    url(r'^buscar_release/$','buscar_release_view', name= 'vista_buscar_release'),
)
