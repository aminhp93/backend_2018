from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import Stock


def get_default_attributes(data):
    return {
        'id': data.id,
        'Symbol': data.Symbol,
        'Close': data.Close,
        'Volume': data.Volume,
        'RSI_14': data.RSI_14,
        'RSI_14_diff': data.RSI_14_diff,
        'ROE': data.ROE,
        'EPS': data.EPS,
        'MarketCapitalization': data.MarketCapitalization,
        'today_capitalization': data.today_capitalization,
        'percentage_change_in_price': data.percentage_change_in_price,
        'percentage_change_in_volume': data.percentage_change_in_volume,
    }


@csrf_exempt
def get_all_stocks(request):
    all_stocks = Stock.objects.all()
    result = []
    for stock in all_stocks:
        result.append(get_default_attributes(stock))
    return JsonResponse({'stocks': result})


@csrf_exempt
def get_quick_filtered_stocks(request):
    filtered_stocks = Stock.objects.filter(Q(Volume__gt=10000) & Q(
        RSI_14__gt=60) & Q(RSI_14__lt=70) & Q(RSI_14_diff__gt=0) & Q(ROE__gt=17) & Q(EPS__gt=3000))
    result = []
    for stock in filtered_stocks:
        result.append(get_default_attributes(stock))
    return JsonResponse({'stocks': result})


@csrf_exempt
def filter_stock(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        result = []
        if 'watching_stocks' in body:
            watching_stocks = body['watching_stocks']
            filtered_stocks = Stock.objects.filter(Symbol__in=watching_stocks)
            for stock in filtered_stocks:
                result.append(get_default_attributes(stock))
            return JsonResponse({'stocks': result})
        Volume_min = 0
        RSI_14_max = 1000000
        RSI_14_min = 0
        RSI_14_diff_min = 0
        ROE_min = 0
        EPS_min = 0
        if 'Volume_min' in body:
            Volume_min = body['Volume_min']
        if 'RSI_14_max' in body:
            RSI_14_max = body['RSI_14_max']
        if 'RSI_14_min' in body:
            RSI_14_min = body['RSI_14_min']
        if 'RSI_14_diff_min' in body:
            RSI_14_diff_min = body['RSI_14_diff_min']
        if 'ROE_min' in body:
            ROE_min = body['ROE_min']
        if 'EPS_min' in body:
            EPS_min = body['EPS_min']
        print(Volume_min, RSI_14_max, RSI_14_min,
              RSI_14_diff_min, ROE_min, EPS_min)
        filtered_stocks = Stock.objects.filter(Q(Volume__gt=Volume_min) & Q(
            RSI_14__gt=RSI_14_min) & Q(RSI_14__lt=RSI_14_max) & Q(RSI_14_diff__gt=RSI_14_diff_min) & Q(ROE__gt=ROE_min) & Q(EPS__gt=EPS_min))
        for stock in filtered_stocks:
            result.append(get_default_attributes(stock))
        return JsonResponse({'stocks': result})
    return JsonResponse({'data': 'Invalid request'})


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
        if 'today_capitalization' in body:
            stock.today_capitalization = body['today_capitalization']
        if 'percentage_change_in_volume' in body:
            stock.percentage_change_in_volume = body['percentage_change_in_volume']
        if 'percentage_change_in_price' in body:
            stock.percentage_change_in_price = body['percentage_change_in_price']
        url = "https://svr1.fireant.vn/api/Data/Finance/LastestFinancialInfo"
        querystring = {"symbol": body['Symbol']}
        headers = {
            'cache-control': "no-cache",
            'postman-token': "8d5daf06-af9e-eb5f-6cf7-c137ac9c9c5e"
        }
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        if response.text != 'null':
            latestFinancialData = json.loads(response.text)
            if 'ROE' in latestFinancialData and type(latestFinancialData['ROE']) == float:
                stock.ROE = latestFinancialData['ROE'] * 100
            if 'EPS' in latestFinancialData and type(latestFinancialData['EPS']) == float:
                stock.EPS = latestFinancialData['EPS']
            if 'MarketCapitalization' in latestFinancialData and type(latestFinancialData['MarketCapitalization']) == float:
                stock.MarketCapitalization = latestFinancialData['MarketCapitalization'] / 10**9
        stock.financial_data = response.text
        stock.save()
        if not stock.id:
            return JsonResponse({'data': 'Created failed'})
        return JsonResponse({'data': 'Created successfully', 'stock': get_default_attributes(stock)})
    return JsonResponse({'data': 'Invalid request'})

@csrf_exempt
def update_stock(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'Symbol' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_symbol = body['Symbol']
        filter_symbols = Post.objects.filter(Symbol=search_symbol)
        if len(filter_symbols) == 1:
            symbol = filter_symbols[0]
            if 'Volume' in body:
                symbol.Volume = body['Volume']
            if 'Close' in body:
                symbol.Close = body['Close']
            symbol.save()
            return JsonResponse({'data': 'Updated successfully', 'post': get_default_attributes(symbol)})
        return JsonResponse({'data': 'Item not found'})
    return JsonResponse({'data': 'Invalid request'})

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
