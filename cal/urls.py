from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from handlers import CalendarHandler, TodoHandler

urlpatterns = patterns('cal.views',
    url(r'^$', 'index', name="index"),
    url(r'^public/(?P<id>[^/]+)/$', 'public', name="public"),
    url(r'^share/(?P<id>[^/]+)/$', 'share', name="share"),
    url(r'^unshare/(?P<id>[^/]+)/$', 'unshare', name="unshare"),

    url(r'^todos/$', 'todos', name="todos"),
    url(r'^todos/(?P<id>[^/]+)/$', 'todos', name="todos"),

    # API handlers
    url(r'^api/calendar/(?P<id>[^/]+)/$', Resource(CalendarHandler)),
    url(r'^api/todo/(?P<id>[^/]+)/$', Resource(TodoHandler)),
)