import json
import dateutil.parser
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import Calendar, Todo
from accounts.models import UserProfile


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


@login_required
def public(request, id):
    if request.method == 'GET':
        try:
            cal = Calendar.objects.get(id=id, public=True)
            owner = UserProfile.objects.get(calendar=cal).user
            return render_to_response('public_index.html', {'owner': owner}, context_instance=RequestContext(request))
        except Exception:
            # BAD request ... calendar is not public we should render a template for this
            return HttpResponse('Calendar not public')


@login_required
def share(request, id):
    if request.method == 'POST':
        cal = Calendar.objects.get(id=id)
        cal.public = True
        cal.save()
        return HttpResponse(json.dumps(cal.to_hash()), content_type='application/json')


@login_required
def unshare(request, id):
    if request.method == 'POST':
        cal = Calendar.objects.get(id=id)
        cal.public = False
        cal.save()
        return HttpResponse(json.dumps(cal.to_hash()), content_type='application/json')


@login_required
def todos(request, id=None):
    current_calendar = request.user.get_profile().calendar if not id else Calendar.objects.get(id=id)
    if request.method == 'POST':
        #TODO: test JSON
        result = json.loads(request.raw_post_data)
        print result
        start = dateutil.parser.parse(result['start']).astimezone(dateutil.tz.tzutc())
        print start
        todo = Todo.objects.create(title=result['title'], start=start,
            calendar=current_calendar)
        return HttpResponse(json.dumps(todo.to_hash()), content_type='application/json')
    else:
        todos = [todo.to_hash(ignore_cal=True) for todo in Todo.objects.filter(calendar__id=current_calendar.id)]
        return HttpResponse(json.dumps(todos), content_type='application/json')
