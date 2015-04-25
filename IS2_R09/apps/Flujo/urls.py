# -*- encoding: utf-8 -*-
"""
    URLS
    ====
    
    Modulo que controla las urls de las L{Vistas<IS2_R09.apps.Flujo.views>} utilizadas en
    L{Flujo<IS2_R09.apps.Flujo>}.
"""
from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Flujo.views',
    url(r'^crear_flujo/$','crear_flujo_view', name= 'vista_crear_flujo'),
    url(r'^adm_flujo/$','adm_flujo_view', name= 'vista_adm_flujo'),
    url(r'^crear_actividad/$','crear_actividad_view', name= 'vista_crear_actividad'),
    url(r'^crear_actividad/flujo/(?P<id_flujo>.*)/$','crear_actividad_from_mod_view', name= 'vista_crear_actividad_modflujo'),
    #url(r'^asignar_equipo/proyecto/(?P<id_proyecto>.*)/$','asignar_equipo_view', name= 'vista_asignar_equipo'),
    #url(r'^cantidad_equipo/proyecto/(?P<id_proyecto>.*)/$','cantidad_equipo_view', name= 'vista_cant_equipo'),
    url(r'^modificar/flujo/(?P<id_flujo>.*)/$','modificar_flujo_view', name= 'vista_modificar_flujo'),
    url(r'^eliminar/flujo/(?P<id_flujo>.*)/$','eliminar_flujo_view', name= 'vista_eliminar_flujo'),
    url(r'^consultar/flujo/(?P<id_flujo>.*)/$','consultar_flujo_view', name= 'vista_consultar_flujo'),
    url(r'^buscar_flujo/$','buscar_flujo_view', name= 'vista_buscar_flujo'),
)
