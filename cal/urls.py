from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('cal.views',
    url(r'^$', 'index', name="index"),
)