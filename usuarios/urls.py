from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuarios.views',
    url(r'^cuenta/(?P<user>\w+)$', 'perfil', name='perfil'),
    url(r'^logout/$', 'logout', name='logout'),
)