from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import Stock
import requests


@csrf_exempt
def get_all_stocks(request):
    all_stocks = Stock.objects.all()
    result = []
    for stock in all_stocks:
        result.append({
            'id': stock.id,
            'Symbol': stock.Symbol,
            'price_data': stock.price_data,
            'financial_data': stock.financial_data
        })
    return JsonResponse({'stocks': result})


@csrf_exempt
def get_quick_filtered_stocks(request):
    filtered_stocks = Stock.objects.filter(Q(Volume__gt=10000) & Q(
        RSI_14__gt=60) & Q(RSI_14__lt=70) & Q(RSI_14_diff__gt=0))
    result = []
    for stock in filtered_stocks:
        result.append({
            'id': stock.id,
            'Symbol': stock.Symbol,
            'Close': stock.Close,
            'Volume': stock.Volume,
            'RSI_14': stock.RSI_14,
            'RSI_14_diff': stock.RSI_14_diff
        })
    return JsonResponse({'stocks': result})


@csrf_exempt
def create_stock(request):
    if request.method == 'POST':
        stock = Stock()
        body = json.loads(request.body.decode('utf-8'))
        if not 'Symbol' in body:
            return JsonResponse({'data': 'Invalid data'})
        stock.Symbol = body['Symbol']
        if not 'price_data' in body:
            return JsonResponse({'data': 'Invalid data'})
        stock.price_data = body['price_data']
        if 'Close' in body:
            stock.Close = body['Close']
        if 'Volume' in body:
            stock.Volume = body['Volume']
        if 'RSI_14' in body:
            stock.RSI_14 = body['RSI_14']
        if 'RSI_14_diff' in body:
            stock.RSI_14_diff = body['RSI_14_diff']
        url = "https://svr1.fireant.vn/api/Data/Finance/LastestFinancialInfo"
        querystring = {"symbol": body['Symbol']}
        headers = {
            'cache-control': "no-cache",
            'postman-token': "8d5daf06-af9e-eb5f-6cf7-c137ac9c9c5e"
        }
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        print(response.text)
        stock.financial_data = response.text
        stock.save()
        if not stock.id:
            return JsonResponse({'data': 'Created failed'})
        return JsonResponse({'data': 'Created successfully', 'stock': {
            'id': stock.id,
            'Symbol': stock.Symbol,
            'price_data': stock.price_data,
            'financial_data': stock.financial_data
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


@csrf_exempt
def delete_all_stocks(request):
    if request.method == 'POST':
        Stock.objects.all().delete()
        return JsonResponse({'data': 'Deleted all stocks successfully'})
    return JsonResponse({'data': 'Deteled all stocks failed'})
