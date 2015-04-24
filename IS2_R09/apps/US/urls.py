# -*- encoding: utf-8 -*-

"""
    Modulo que controla las urls de las L{views<IS2_R09.apps.US.views>}   
    @author: Samuel Ruiz,Melissa Bogado,Rafael Ricardo
"""
__docformat__ = "Epytext" 
from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.US.views',
    url(r'^crear_US/$','crear_us_view', name= 'vista_crear_us'),
    url(r'^adm_US/$','adm_us_view', name= 'vista_adm_us'),
    #url(r'^asignar_equipo/proyecto/(?P<id_proyecto>.*)/$','asignar_equipo_view', name= 'vista_asignar_equipo'),
    #url(r'^cantidad_equipo/proyecto/(?P<id_proyecto>.*)/$','cantidad_equipo_view', name= 'vista_cant_equipo'),
    url(r'^modificar/US/(?P<id_us>.*)/$','modificar_us_view', name= 'vista_modificar_us'),
    url(r'^eliminar/US/(?P<id_us>.*)/$','eliminar_us_view', name= 'vista_eliminar_us'),
    url(r'^consultar/US/(?P<id_us>.*)/$','consultar_us_view', name= 'vista_consultar_us'),
    #url(r'^buscar_proyecto/$','buscar_proyecto_view', name= 'vista_buscar_proyecto'),
)
