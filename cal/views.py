import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def json_test(request):
    result = json.dumps({'test': 'hello json'})
    return HttpResponse(result, content_type='application/json')
    