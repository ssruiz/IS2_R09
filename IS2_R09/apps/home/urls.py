# -*- encoding: utf-8 -*-
"""
    URLS
    ====
    
    Módulo que controla las urls de las L{Vistas<IS2_R09.apps.home.views>} utilizadas en
    L{Home<IS2_R09.apps.home>}.
"""
from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.home.views',
    url(r'^$','index_view', name= 'vista_index'),
    url(r'^login/$','login_view', name= 'vista_login'),
    url(r'^logout/$','logout_view', name= 'vista_logout'),
    url(r'^menu/$','menu_view', name= 'vista_menu'),
    url(r'^passw_recovery/$','recuperar_pass_view', name= 'vista_rp'),
)
