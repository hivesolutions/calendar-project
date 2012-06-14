import json
from piston.handler import BaseHandler
from models import Calendar, Todo
from django.http import HttpResponse



class CalendarHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, id):
        result = {'todos': [todo.to_hash() for todo in Todo.objects.filter(calendar__id=id)]}
        return HttpResponse(json.dumps(result), content_type='application/json')


class TodoHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'DELETE')

    def read(self, request, id):
        todo = Todo.objects.get(id=id)
        return HttpResponse(json.dumps(todo.to_hash()), content_type='application/json')

    def create(self):
        pass

    def delete(self):
        pass

