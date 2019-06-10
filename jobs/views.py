from django.shortcuts import render
from .models import Job
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from helpers.errorMessages import message
import json


def get_default_attributes(data):
    return {
        'id': data.id,
        # 'time': data.time,
        # 'searchWord': data.searchWord,
        'content': data.content
    }
# Create your views here.


@csrf_exempt
def job_list(request):
    # return JsonResponse({})
    all_jobs = Job.objects.all()
    # print(111, all_jobs)
    # return JsonResponse({})
    result = []
    for job in all_jobs:
        result.append(get_default_attributes(job))
    return JsonResponse({'jobs': result})


@csrf_exempt
def job_create(request):
    if request.method == 'POST':
        job = Job()
        body = json.loads(request.body.decode('utf-8'))
        if not 'time' in body:
            return JsonResponse({'data': "Invalid data"})
        job.time = body['time']
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
def job_detail(request, pk):
    return JsonResponse({'data': 'detail'})


@csrf_exempt
def job_update(request, pk):
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
            if 'time' in body:
                job.time = body['time']
            job.save()
            return JsonResponse({'data': 'Updated successfully', 'job': get_default_attributes(job)})
        return JsonResponse({'data': 'Item not found'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def job_delete(request, pk):
    if request.method == 'POST':
        return JsonResponse({'data': 'delete'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def job_last(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'searchWord' in body:
            return JsonResponse({'data': "Invalid data"})
        searchWord = body['searchWord']
        filtered_jobs = Job.objects.filter(
            searchWord=searchWord).order_by('-time')
        if len(filtered_jobs) == 0:
            return JsonResponse({'job': ''})
        return JsonResponse({'job': get_default_attributes(filtered_jobs[0])})
    return JsonResponse({'data': 'Invalid request'})
