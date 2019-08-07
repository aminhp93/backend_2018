from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Config
# Create your views here.

@csrf_exempt
def update(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'date' in body:
            return JsonResponse({'data': 'error'})
        configs = Config.objects.filter(key='LAST_UPDATED_TIME')
        if len(configs) > 0:
            last_updated_time = configs[0]
            last_updated_time.value = body['date']
            last_updated_time.save()
            return JsonResponse({'data': 'LAST_UPDATED_TIME success'})
        return JsonResponse({'data': 'error'})
    return JsonResponse({'data': 'error'})

def get_last_updated_time(request):
    configs = Config.objects.filter(key='LAST_UPDATED_TIME')
    if len(configs) > 0:
        return JsonResponse({'data': configs[0].value})
    return JsonResponse({'data': 'error'})
        
