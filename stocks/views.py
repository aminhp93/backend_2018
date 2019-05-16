from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import Stock


@csrf_exempt
def get_all_stocks(request):
    all_stocks = Stock.objects.all()
    result = []
    for stock in all_stocks:
        result.append({
            'id': stock.id,
            'symbol': stock.symbol,
            'price_data': stock.price_data
        })
    return JsonResponse({'stocks': result})


@csrf_exempt
def create_stock(request):
    if request.method == 'POST':
        stock = Stock()
        body = json.loads(request.body.decode('utf-8'))
        if not 'symbol' in body:
            return JsonResponse({'data': 'Invalid data'})
        stock.symbol = body['symbol']
        if not 'price_data' in body:
            return JsonResponse({'data': 'Invalid data'})
        stock.price_data = body['price_data']
        stock.save()
        if not stock.id:
            return JsonResponse({'data': 'Created failed'})
        return JsonResponse({'data': 'Created successfully', 'stock': {
            'id': stock.id,
            'symbol': stock.symbol,
            'price_data': stock.price_data
        }})
    return JsonResponse({'data': 'Invalid request'})

# @csrf_exempt
# def update_stock(request):
#     if request.method == 'POST':
#         body = json.loads(request.body.decode('utf-8'))
#         if not 'id' in body:
#             return JsonResponse({'data': 'Invalid data'})
#         search_id = body['id']
#         if 'is_done' in body:
#             filter_posts = Post.objects.filter(id=search_id)
#             if len(filter_posts) == 1:
#                 post = filter_posts[0]
#                 post.is_done = body['is_done']
#                 if body['is_done'] == True:
#                     post.is_doing = False
#                 post.save()
#                 return JsonResponse({'data': 'Updated successfully', 'post': {
#                     'id': post.id,
#                     'content': post.content,
#                     'is_done': post.is_done,
#                     'is_doing': post.is_doing,
#                     'assignee_id': post.assignee_id,
#                     'progress_percent': post.progress_percent
#                 }})
#             return JsonResponse({'data': 'Item not found'})
#         return JsonResponse({'data': 'Invalid request'})
#     return JsonResponse({'data': 'Invalid request'})

# @csrf_exempt
# def delete_post(request):
#     if request.method == 'POST':
#         body = json.loads(request.body.decode('utf-8'))
#         if not 'id' in body:
#             return JsonResponse({'data': 'Invalid data'})
#         search_id = body['id']
#         post = Post.objects.filter(id=search_id).delete()
#         if post[0] == 1:
#             return JsonResponse({'data': 'Deleted successfully'})
#         else:
#             return JsonResponse({'data': 'Deleted failed'})
