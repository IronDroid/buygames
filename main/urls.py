from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'main', name='main'),
    url(r'^plataforma/$', 'plataforma', name='plataforma'),
    url(r'^genero/$', 'genero', name='genero'),
    url(r'^detail/(?P<idp>\d+)$', 'detail', name='detail'),
)