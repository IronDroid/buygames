from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuarios.views',
    url(r'^cuenta/(?P<user>\w+)$', 'perfil', name='perfil'),
    url(r'^delete/(?P<user>\w+)$', 'delete', name='delete'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^compras/$', 'detalle_compra', name='detalle_compra'),
)