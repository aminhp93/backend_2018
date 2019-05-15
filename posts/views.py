from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import Post


@csrf_exempt
def get_all_posts(request):
    all_posts = Post.objects.all()
    result = []
    for post in all_posts:
        result.append({
            'id': post.id,
            'content': post.content,
            'is_done': post.is_done,
            'is_doing': post.is_doing,
            'assignee_id': post.assignee_id,
            'progress_percent': post.progress_percent
        })
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
        return JsonResponse({'data': 'Created successfully', 'post': {
            'id': post.id,
            'content': post.content,
            'is_done': post.is_done,
            'is_doing': post.is_doing,
            'assignee_id': post.assignee_id,
            'progress_percent': post.progress_percent
        }})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def update_post(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'id' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_id = body['id']
        if 'is_done' in body:
            filter_posts = Post.objects.filter(id=search_id)
            if len(filter_posts) == 1:
                post = filter_posts[0]
                post.is_done = body['is_done']
                if body['is_done'] == True:
                    post.is_doing = False
                post.save()
                return JsonResponse({'data': 'Updated successfully', 'post': {
                    'id': post.id,
                    'content': post.content,
                    'is_done': post.is_done,
                    'is_doing': post.is_doing,
                    'assignee_id': post.assignee_id,
                    'progress_percent': post.progress_percent
                }})
            return JsonResponse({'data': 'Item not found'})
        if 'is_doing' in body:
            filter_posts = Post.objects.filter(id=search_id)
            if len(filter_posts) == 1:
                post = filter_posts[0]
                if body['is_doing'] == True:
                    for item in Post.objects.all():
                        item.is_doing = False
                        item.save()
                post.is_doing = body['is_doing']
                post.save()
                return JsonResponse({'data': 'Updated successfully', 'post': {
                    'id': post.id,
                    'content': post.content,
                    'is_done': post.is_done,
                    'is_doing': post.is_doing,
                    'assignee_id': post.assignee_id,
                    'progress_percent': post.progress_percent
                }})
            return JsonResponse({'data': 'Item not found'})
        if 'content' in body:
            filter_posts = Post.objects.filter(id=search_id)
            if len(filter_posts) == 1:
                post = filter_posts[0]
                post.content = body['content']
                post.save()
                return JsonResponse({'data': 'Updated successfully', 'post': {
                    'id': post.id,
                    'content': post.content,
                    'is_done': post.is_done,
                    'is_doing': post.is_doing,
                    'assignee_id': post.assignee_id,
                    'progress_percent': post.progress_percent
                }})
            return JsonResponse({'data': 'Item not found'})
        if 'assignee_id' in body:
            filter_posts = Post.objects.filter(id=search_id)
            if len(filter_posts) == 1:
                post = filter_posts[0]
                post.assignee_id = body['assignee_id']
                post.save()
                return JsonResponse({'data': 'Updated successfully', 'post': {
                    'id': post.id,
                    'content': post.content,
                    'is_done': post.is_done,
                    'is_doing': post.is_doing,
                    'assignee_id': post.assignee_id,
                    'progress_percent': post.progress_percent
                }})
            return JsonResponse({'data': 'Item not found'})
        if 'progress_percent' in body:
            filter_posts = Post.objects.filter(id=search_id)
            if len(filter_posts) == 1:
                post = filter_posts[0]
                post.progress_percent = body['progress_percent']
                post.save()
                return JsonResponse({'data': 'Updated successfully', 'post': {
                    'id': post.id,
                    'content': post.content,
                    'is_done': post.is_done,
                    'is_doing': post.is_doing,
                    'assignee_id': post.assignee_id,
                    'progress_percent': post.progress_percent
                }})
            return JsonResponse({'data': 'Item not found'})
        return JsonResponse({'data': 'Invalid request'})
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
