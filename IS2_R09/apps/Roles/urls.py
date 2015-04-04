from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Roles.views',
    url(r'^adm_rol/$','adm_rol_view', name= 'vista_adm_rol'),
    url(r'^crear_rol/$','crear_rol_view', name= 'vista_crear_rol'),
    url(r'^modificar/rol/(?P<id_rol>.*)/$','modificar_rol_view', name= 'vista_mod_rol'),
    url(r'^eliminar/rol/(?P<id_rol>.*)/$','eliminar_rol_view', name= 'vista_eliminar_rol'),
    url(r'^consultar/rol/(?P<id_rol>.*)/$','consultar_rol_view', name= 'vista_consultar_rol'),
    url(r'^buscar_rol/$','buscar_rol_view', name= 'vista_buscar_rol'),
    
)
