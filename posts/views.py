from django.shortcuts import render
import time
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import Post
from django.db.models import Q


def get_default_attributes(obj):
    return {
        'id': obj.id,
        'content': obj.content,
        'is_done': obj.is_done,
        'default_cost': obj.default_cost,
        'actual_cost': obj.actual_cost,
        'update': obj.update,
        'timestamp': obj.timestamp,
        'scheduled_time': obj.scheduled_time,
        'done_time': obj.done_time
    }


@csrf_exempt
def get_all_posts(request):
    yesterday_miliseconds = time.time()*1000 - 86400000
    all_posts = Post.objects.all().exclude(Q(is_done=True) & Q(
        done_time__lt=yesterday_miliseconds)).order_by('scheduled_time')
    result = []
    for post in all_posts:
        result.append(get_default_attributes(post))
    return JsonResponse({'posts': result})


@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        post = Post()
        post.title = 'title'
        body = json.loads(request.body.decode('utf-8'))
        if not 'content' in body:
            return JsonResponse({'data': 'Invalid data'})
        post.content = body['content']
        post.save()
        if not post.id:
            return JsonResponse({'data': 'Created failed'})
        post.title = 'title ' + str(post.id)
        post.save()
        return JsonResponse({'data': 'Created successfully', 'post': get_default_attributes(post)})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def update_post(request):
    if request.method == 'POST':
        print(request, request.body.decode('utf-8'))
        body = json.loads(request.body.decode('utf-8'))
        if not 'id' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_id = body['id']
        filter_posts = Post.objects.filter(id=search_id)
        if len(filter_posts) == 1:
            post = filter_posts[0]
            if 'is_done' in body:
                post.is_done = body['is_done']
                if body['is_done'] == True:
                    post.is_doing = False
            if 'done_time' in body:
                post.done_time = body['done_time']
            if 'is_doing' in body:
                if body['is_doing'] == True:
                    for item in Post.objects.all():
                        item.is_doing = False
                        item.save()
                post.is_doing = body['is_doing']
            if 'content' in body:
                post.content = body['content']
            if 'assignee_id' in body:
                post.assignee_id = body['assignee_id']
            if 'progress_percent' in body:
                post.progress_percent = body['progress_percent']
            if 'default_cost' in body:
                try:
                    post.default_cost = float(body['default_cost'])
                except ValueError:
                    return JsonResponse({'data': 'Invalid type data'})
            if 'actual_cost' in body:
                try:
                    post.actual_cost = float(body['actual_cost'])
                except ValueError:
                    return JsonResponse({'data': 'Invalid type data'})
            if 'scheduled_time' in body:
                try:
                    post.scheduled_time = round(
                        float(body['scheduled_time']), 2)
                except ValueError:
                    return JsonResponse({'data': 'Invalid type data'})
                a = Post.objects.filter(scheduled_time=post.scheduled_time)
                while len(a) > 0:
                    post.scheduled_time = round(post.scheduled_time + 0.01, 2)
                    a = Post.objects.filter(scheduled_time=post.scheduled_time)
            post.save()
            return JsonResponse({'data': 'Updated successfully', 'post': get_default_attributes(post)})
        return JsonResponse({'data': 'Item not found'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def delete_post(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'id' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_id = body['id']
        post = Post.objects.filter(id=search_id).delete()
        if post[0] == 1:
            return JsonResponse({'data': 'Deleted successfully'})
        else:
            return JsonResponse({'data': 'Deleted failed'})
