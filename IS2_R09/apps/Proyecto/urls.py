from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Proyecto.views',
    url(r'^crear_proyecto/$','crear_proyecto_view', name= 'vista_crear_proyecto'),
    url(r'^adm_proyecto/$','adm_proyecto_view', name= 'vista_adm_proyecto'),
    url(r'^asignar_equipo/proyecto/(?P<id_proyecto>.*)/$','asignar_equipo_view', name= 'vista_asignar_equipo'),
    url(r'^cantidad_equipo/proyecto/(?P<id_proyecto>.*)/$','cantidad_equipo_view', name= 'vista_cant_equipo'),
)
