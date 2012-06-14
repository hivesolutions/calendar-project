from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from handlers import CalendarHandler, TodoHandler

urlpatterns = patterns('cal.views',
    url(r'^$', 'index', name="index"),
    url(r'^json/$', 'json_test', name="json"),
    url(r'^api/calendar/(?P<id>[^/]+)/$', Resource(CalendarHandler)),
    url(r'^api/todo/(?P<id>[^/]+)/$', Resource(TodoHandler)),
)