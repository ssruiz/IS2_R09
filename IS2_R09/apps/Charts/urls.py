from django.conf.urls import patterns,url


urlpatterns = patterns('IS2_R09.apps.Charts.views',
    url(r'^bd_load/$','bd_load', name= 'load_bd'),
)
