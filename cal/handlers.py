from piston.handler import BaseHandler
from piston.utils import rc
from models import Calendar, Todo
from accounts.models import UserProfile
from django.http import HttpResponse
import json
import settings

#TODO: make this one a decorator
def is_authenticated(request):
    auth_header = getattr(settings, 'AUTH_HEADER')
    auth_header = 'HTTP_%s' % (auth_header.upper().replace('-', '_'))
    auth_string = request.META.get(auth_header)
    try:
      return UserProfile.objects.get(api_key=auth_string)
    except Exception:
      return None


class CalendarHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, id):
        profile = is_authenticated(request)
        if profile and profile.calendar.id == id:
          todos = Todo.objects.filter(calendar__id=id)
          result = {'todos': [todo.to_hash(ignore_cal=True) for todo in todos]}
          return HttpResponse(json.dumps(result), content_type='application/json')
        else:
          return rc.FORBIDDEN


class TodoHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'DELETE')

    def read(self, request, id):
        if is_authenticated(request):
          todo = Todo.objects.get(id=id)
          return HttpResponse(json.dumps(todo.to_hash()), content_type='application/json')
        else:
          return rc.FORBIDDEN

    def create(self):
        pass

    def delete(self):
        pass

