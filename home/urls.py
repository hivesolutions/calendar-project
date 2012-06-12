from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name="index"),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'home/login.html'}),
)