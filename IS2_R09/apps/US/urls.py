from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.US.views',
    url(r'^crear_US/$','crear_us_view', name= 'vista_crear_us'),
    url(r'^adm_US/$','adm_us_view', name= 'vista_adm_us'),
    #url(r'^asignar_equipo/proyecto/(?P<id_proyecto>.*)/$','asignar_equipo_view', name= 'vista_asignar_equipo'),
    #url(r'^cantidad_equipo/proyecto/(?P<id_proyecto>.*)/$','cantidad_equipo_view', name= 'vista_cant_equipo'),
    #url(r'^modificar/proyecto/(?P<id_proyecto>.*)/$','modificar_proyecto_view', name= 'vista_modificar_proyecto'),
    #url(r'^eliminar/proyecto/(?P<id_proyecto>.*)/$','eliminar_proyecto_view', name= 'vista_eliminar_proyecto'),
    #url(r'^consultar/proyecto/(?P<id_proyecto>.*)/$','consultar_proyecto_view', name= 'vista_consultar_proyecto'),
    #url(r'^buscar_proyecto/$','buscar_proyecto_view', name= 'vista_buscar_proyecto'),
)
