from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
import datetime

def test(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return JsonResponse({'foo': 'bar'})