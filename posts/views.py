from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import Post

@csrf_exempt
def get_all_posts(request):
    all_posts = Post.objects.all()
    print(all_posts)
    result = {}
    for post in all_posts:
        result[post.id] = post.content
    print(result)
    return JsonResponse({'all_posts': result})

@csrf_exempt
def create_post(request):
    print(request.POST.dict())
    if request.method == 'POST':
        post = Post()
        print(post.id)
        post.title = 'title'
        post.content = request.POST.dict()['data']
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