from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IS2_R09.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('IS2_R09.apps.home.urls')),
    url(r'^',include('IS2_R09.apps.Usuario.urls')),
    url(r'^',include('IS2_R09.apps.Roles.urls')),
    url(r'^',include('IS2_R09.apps.Proyecto.urls')),
    url(r'^',include('IS2_R09.apps.Flujo.urls')),
    url(r'^',include('IS2_R09.apps.US.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT}),
)
