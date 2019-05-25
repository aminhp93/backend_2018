from django.shortcuts import render
from .models import Job
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from helpers.errorMessages import message
import json


def get_default_attributes(data):
    return {
        'id': data.id,
        'timestamp': data.timestamp,
        'searchWord': data.searchWord,
        'content': data.content
    }
# Create your views here.


@csrf_exempt
def get_all_jobs(request):
    all_jobs = Job.objects.all()
    result = []
    for job in all_jobs:
        result.append(get_default_attributes(job))
    return JsonResponse({'jobs': result})


@csrf_exempt
def get_last_job(request):
    filtered_jobs = Job.objects.filter(searchWord='').order_by('-timestamp')
    if len(filtered_jobs) == 0:
        return JsonResponse({'job': ''})
    return JsonResponse({'job': get_default_attributes(filtered_jobs[0])})


@csrf_exempt
def create_job(request):
    if request.method == 'POST':
        job = Job()
        body = json.loads(request.body.decode('utf-8'))
        if not 'timestamp' in body:
            return JsonResponse({'data': "Invalid data"})
        job.timestamp = body['timestamp']
        if 'searchWord' in body:
            job.searchWord = body['searchWord']
        if 'content' in body:
            job.content = body['content']
        job.save()
        if not job.id:
            return JsonResponse({'data': 'Created failed'})
        return JsonResponse({'data': 'Created sucessfully', 'jobs': get_default_attributes(job)})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def update_job(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'id' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_id = body['id']
        filter_jobs = Job.objects.filter(id=search_id)
        if len(filter_jobs) == 1:
            job = filter_jobs[0]
            if 'content' in body:
                job.content = body['content']
            if 'timestamp' in body:
                job.timestamp = body['timestamp']
            job.save()
            return JsonResponse({'data': 'Updated successfully', 'job': get_default_attributes(job)})
        return JsonResponse({'data': 'Item not found'})
    return JsonResponse({'data': 'Invalid request'})
