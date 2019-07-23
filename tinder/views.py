from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import Tinder


def get_default_attributes(data):
    return {
        'id': data.id,
        'user_id': data.user_id,
        'content': data.content,
        'status': data.status,
    }


@csrf_exempt
def tinder_list(request):
    print(request, request.META, request.GET)
    status = 'active'
    if 'status' in request.GET:
        status = request.GET['status']
    content_regex = ''
    if 'q' in request.GET:
        content_regex = request.GET['q']
    tinders = Tinder.objects.filter(
        Q(content__regex=r'{0}'.format(content_regex)) & Q(status=status))
    result = []
    for tinder in tinders:
        if len(result) < 100:
            result.append(get_default_attributes(tinder))
    return JsonResponse({'results': result, 'length': len(tinders)})


@csrf_exempt
def tinder_create(request):
    if request.method == 'POST':
        tinder = Tinder()
        body = json.loads(request.body.decode('utf-8'))
        if not 'user_id' in body:
            return JsonResponse({'data': 'Invalid data'})
        tinder.user_id = body['user_id']
        if not 'content' in body:
            return JsonResponse({'data': 'Invalid data'})
        tinder.content = body['content']
        tinder.save()
        if not tinder.id:
            return JsonResponse({'data': 'Created failed'})
        return JsonResponse({'data': 'Created successfully', 'tinder': get_default_attributes(tinder)})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def tinder_detail(request, pk):
    return JsonResponse({'data': 'detail'})


@csrf_exempt
def tinder_update(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'id' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_id = body['id']
        search_tinders = Tinder.objects.filter(id=search_id)
        print(search_tinders)
        if len(search_tinders) == 1:
            tinder = search_tinders[0]
            if 'status' in body:
                tinder.status = body['status']
            tinder.save()
            return JsonResponse({'data': 'Updated successfully', 'tinder': get_default_attributes(tinder)})
        return JsonResponse({'data': 'Item not found'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def tinder_delete(request, pk):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'id' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_id = body['id']
        tinders = tinder.objects.filter(id=search_id).delete()
        if tinders[0] == 1:
            return JsonResponse({'data': 'Deleted successfully'})
        else:
            return JsonResponse({'data': 'Deleted failed'})


@csrf_exempt
def tinder_delete_all(request):
    if request.method == 'POST':
        Tinder.objects.all().delete()
        return JsonResponse({'data': 'Deleted all tinders successfully'})
    return JsonResponse({'data': 'Deteled all tinders failed'})


@csrf_exempt
def get_quick_filtered_tinders(request):
    filtered_tinders = tinder.objects.filter(Q(Volume__gt=10000) & Q(
        RSI_14__gt=60) & Q(RSI_14__lt=70) & Q(RSI_14_diff__gt=0) & Q(ROE__gt=17) & Q(EPS__gt=3000))
    result = []
    for tinder in filtered_tinders:
        result.append(get_default_attributes(tinder))
    return JsonResponse({'tinders': result})


@csrf_exempt
def tinder_filter(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        result = []
        if 'watching_tinders' in body:
            watching_tinders = body['watching_tinders']
            filtered_tinders = tinder.objects.filter(
                Symbol__in=watching_tinders)
            for tinder in filtered_tinders:
                result.append(get_default_attributes(tinder))
            return JsonResponse({'tinders': result})
        Volume_min = 0
        RSI_14_max = 1000000
        RSI_14_min = -99999999
        RSI_14_diff_min = -99999999
        ROE_min = -99999999
        EPS_min = -99999999
        today_capitalization_min = 0
        percentage_change_in_price_min = -99999999
        Symbol_search = ''
        if 'Symbol_search' in body:
            Symbol_search = body['Symbol_search']
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
        if 'today_capitalization_min' in body:
            today_capitalization_min = body['today_capitalization_min']
        if 'percentage_change_in_price_min' in body:
            percentage_change_in_price_min = body['percentage_change_in_price_min']
        filtered_tinders = tinder.objects.filter(Q(Volume__gt=Volume_min) & Q(RSI_14__gt=RSI_14_min) & Q(RSI_14__lt=RSI_14_max) & Q(RSI_14_diff__gt=RSI_14_diff_min) & Q(ROE__gt=ROE_min) & Q(EPS__gt=EPS_min) & Q(
            today_capitalization__gt=today_capitalization_min) & Q(percentage_change_in_price__gt=percentage_change_in_price_min) & Q(Symbol__regex=r'{0}'.format(Symbol_search))).order_by('-today_capitalization')
        for tinder in filtered_tinders:
            result.append(get_default_attributes(tinder))
        return JsonResponse({'tinders': result})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def analyze(request):
    results = []
    for i in range(1980, 2005):
        regex = 'birth_date\":\"' + str(i)
        count = len(Tinder.objects.filter(content__regex=r'{0}'.format(regex)))
        key = str(i)
        item = {
            'name': key,
            'value': count
        }
        results.append(item)
    print(results)
    return JsonResponse({
        'data': {
            'count': results
        }
    })
