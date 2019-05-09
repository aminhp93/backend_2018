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
    print(all_posts)
    result = []
    for post in all_posts:
        result.append({
            'id': post.id,
            'content': post.content
        })
    print(result)
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
        return JsonResponse({'data': 'Created successfully'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def update_post(request):
    if request.method == 'POST':
        return JsonResponse({'data': 'Updated successfully'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def delete_post(request):
    print(52, request.body)
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        print(body)
        if not 'id' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_id = body['id']
        post = Post.objects.filter(id=search_id).delete()
        if post[0] == 1:
            return JsonResponse({'data': 'Deleted successfully'})
        else:
            return JsonResponse({'data': 'Deleted failed'})
