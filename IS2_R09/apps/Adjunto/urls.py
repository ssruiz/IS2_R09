# -*- encoding: utf-8 -*-
"""
    URLS
    ====
    
    Modulo que controla las urls de las L{Vistas<IS2_R09.apps.Adjunto.views>} utilizadas en
    L{Adjunto<IS2_R09.apps.Adjunto>}.
"""
from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Adjunto.views',
    url(r'^adm_adjunto/(?P<id_us>.*)/$','adm_adjunto_view', name= 'vista_adm_adjunto'),
    url(r'^crear_adjunto/(?P<id_us>.*)/$','crear_adjunto_view', name= 'vista_crear_adjunto'),
    url(r'^modificar/adjunto/(?P<id_adjunto>.*)/(?P<id_us>.*)/$','modificar_adjunto_view', name= 'vista_modificar_adjunto'),
    url(r'^eliminar/adjunto/(?P<id_adjunto>.*)/(?P<id_us>.*)/$','eliminar_adjunto_view', name= 'vista_eliminar_adjunto'),
    url(r'^consultar/adjunto/(?P<id_adjunto>.*)/(?P<id_us>.*)/$','consultar_adjunto_view', name= 'vista_consultar_adjunto'),
)
