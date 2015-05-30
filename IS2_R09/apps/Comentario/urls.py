# -*- encoding: utf-8 -*-
"""
    URLS
    ====
    
    Modulo que controla las urls de las L{Vistas<IS2_R09.apps.Comentario.views>} utilizadas en
    L{Comentario<IS2_R09.apps.Comentario>}.
"""
from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Comentario.views',
    url(r'^adm_comentario/(?P<id_us>.*)/$','adm_comentario_view', name= 'vista_adm_comentario'),
    url(r'^crear_comentario/(?P<id_us>.*)/$','crear_comentario_view', name= 'vista_crear_comentario'),
    url(r'^modificar/comentario/(?P<id_comentario>.*)/(?P<id_us>.*)/$','modificar_comentario_view', name= 'vista_modificar_comentario'),
    url(r'^eliminar/comentario/(?P<id_comentario>.*)/(?P<id_us>.*)/$','eliminar_comentario_view', name= 'vista_eliminar_comentario'),
    url(r'^consultar/comentario/(?P<id_comentario>.*)/(?P<id_us>.*)/$','consultar_comentario_view', name= 'vista_consultar_comentario'),
    url(r'^crear_comentario_us/','crear_comentario_us',name='crear_comentario_us'),
)
