from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Proyecto.views',
    url(r'^crear_proyecto/$','crear_proyecto_view', name= 'vista_crear_proyecto'),
    url(r'^adm_proyecto/$','adm_proyecto_view', name= 'vista_adm_proyecto'),
    url(r'^asignar_equipo/proyecto/(?P<id_proyecto>.*)/$','asignar_equipo_view', name= 'vista_asignar_equipo'),
    url(r'^cantidad_equipo/proyecto/(?P<id_proyecto>.*)/$','cantidad_equipo_view', name= 'vista_cant_equipo'),
    url(r'^modificar/proyecto/(?P<id_proyecto>.*)/$','modificar_proyecto_view', name= 'vista_modificar_proyecto'),
    url(r'^eliminar/proyecto/(?P<id_proyecto>.*)/$','eliminar_proyecto_view', name= 'vista_eliminar_proyecto'),
    url(r'^consultar/proyecto/(?P<id_proyecto>.*)/$','consultar_proyecto_view', name= 'vista_consultar_proyecto'),
    url(r'^buscar_proyecto/$','buscar_proyecto_view', name= 'vista_buscar_proyecto'),
    url(r'kanban/proyecto/(?P<id_proyecto>.*)/$','kanban_proyecto_view', name= 'vista_kanban_proyecto'),
    url(r'^ust_load/$','ustload', name= 'ustload'),
    url(r'^cambiar_estado/$','cambiar_estado', name= 'cambest'),
    url(r'burndownchart/proyecto/(?P<id_proyecto>.*)/$','burndown_chart_view', name= 'burn_chart'),
    url(r'^volver_actividad/$','volver_actividad_view', name= 'volver'),
    url(r'^reporte/proyecto/(?P<id_proyecto>.*)/$','reporte_view', name= 'vista_reporte_proyecto'),
)
