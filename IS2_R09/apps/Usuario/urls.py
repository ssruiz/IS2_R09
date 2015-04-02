from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Usuario.views',
    url(r'^crear_usuario/$','crear_usuario_view', name= 'vista_crear_usuario'),
    url(r'^adm_sesion/$','adm_sesion_view', name= 'vista_adm_sesion'),
    url(r'^mod_datos/$','mod_datos_view', name= 'vista_modificar_datos'),
    url(r'^adm_usuario/$','adm_usuario_view', name= 'vista_adm_usuario'),
    url(r'^modificar/usuario/(?P<id_usuario>.*)/$','modificar_usuario_view', name= 'vista_mod_usuario'),
    url(r'^eliminar/usuario/(?P<id_usuario>.*)/$','eliminar_usuario_view', name= 'vista_mod_usuario'),
)
