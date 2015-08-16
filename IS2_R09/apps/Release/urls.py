# -*- encoding: utf-8 -*-

"""
    Modulo que controla las urls de las L{views<IS2_R09.apps.Release.views>}   
    @author: Samuel Ruiz,Melissa Bogado,Rafael Ricardo
"""
__docformat__ = "Epytext" 
from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Release.views',
    url(r'^sacar_release/$','sacar_release_view', name= 'vista_sacar_release'),
    url(r'^lanzar_release/$','lanzar_release_view', name= 'vista_lanzar_release'),
)
