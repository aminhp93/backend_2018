from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import Stock
from core.models import Config
import re
from datetime import datetime
from helpers.functionUtils import (
    count_trading_times,
    find_index_array_object,
    array_test,
    find_index_array_string,
    range_date_to_update
)

from posts.models import Post
from helpers.constants import (
    date_2012, 
    date_2013, 
    date_2014, 
    date_2015, 
    date_2016,
    date_2017,
    date_2018,
    date_2019
)


def get_default_attributes(data):
    return {
        'id': data.id,
        'Symbol': data.Symbol,
        'yesterday_Close': data.yesterday_Close,
        'Close': data.Close,
        'Volume': data.Volume,
        'RSI_14': data.RSI_14,
        'RSI_14_diff': data.RSI_14_diff,
        'ROE': data.ROE,
        'EPS': data.EPS,
        'Date': data.Date,
        'Open': data.Open,
        'High': data.High,
        'Low': data.Low,
        'MarketCapitalization': data.MarketCapitalization,
        'today_capitalization': data.today_capitalization,
        'percentage_change_in_price': data.percentage_change_in_price,
        'percentage_change_in_volume': data.percentage_change_in_volume,
    }


def get_analyze_attributes(data, percent, period):
    data1 = json.loads(data.price_data)
    result = []
    for i in range(0, len(data1) - period):
        if data1[i]["Close"] * percent < data1[i + period]["High"]:
            result.append(data1[i]["Date"])

    return {
        'result': result,
        'Symbol': data.Symbol
    }


@csrf_exempt
def stock_list(request):
    all_stocks = Stock.objects.filter(Date=date_2019()[-22:])
    result = []
    for stock in all_stocks:
        result.append(get_default_attributes(stock))
    return JsonResponse({'stocks': result})


@csrf_exempt
def stock_create(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'Symbol' in body:
            return JsonResponse({'data': 'Invalid data'})
        if not 'price_data' in body:
            return JsonResponse({'data': 'Invalid data'})
        if not 'Year' in body:
            return JsonResponse({'data': 'Invalid data'})
        price_data = json.loads(body['price_data'])
        Year = body['Year']
        if Year == '2012':
            range_date = date_2012()
        elif Year == '2013':
            range_date = date_2013()
        elif Year == '2014':
            range_date = date_2014()
        elif Year == '2015':
            range_date = date_2015()
        elif Year == '2016':
            range_date = date_2016()
        elif Year == '2017':
            range_date = date_2017()
        elif Year == '2018':
            range_date = date_2018()
        elif Year == '2019':
            range_date = range_date_to_update()
        else:
            range_date = range_date_to_update()
        for i in range(len(price_data)):
            match = re.search(r'{0}'.format(price_data[i]['Date']), range_date)
            if match is None:
                continue
            stock = Stock()
            stock.Symbol = price_data[i]['Symbol']
            stock.Close = price_data[i]['Close']
            stock.Open = price_data[i]['Open']
            stock.High = price_data[i]['High']
            stock.Low = price_data[i]['Low']
            stock.Volume = price_data[i]['Volume']
            stock.Value = price_data[i]['Value']
            stock.Date = price_data[i]['Date']
        # if 'RSI_14' in body:
        #     stock.RSI_14 = body['RSI_14']
        # if 'RSI_14_diff' in body:
        #     stock.RSI_14_diff = body['RSI_14_diff']
        # if 'today_capitalization' in body:
            stock.today_capitalization = stock.Volume * stock.Close
            if stock.Symbol == price_data[i - 1]['Symbol']:
                # print(stock.Close, price_data[i - 1]['Symbol'])
                stock.percentage_change_in_price = (stock.Close - price_data[i - 1]['Close'])/price_data[i - 1]['Close']
            
        # if 'percentage_change_in_volume' in body:
        #     stock.percentage_change_in_volume = body['percentage_change_in_volume']
        # if 'percentage_change_in_price' in body:
        #     stock.percentage_change_in_price = body['percentage_change_in_price']
        # url = "https://svr1.fireant.vn/api/Data/Finance/LastestFinancialInfo"
        # querystring = {"symbol": body['Symbol']}
        # headers = {
        #     'cache-control': "no-cache",
        #     'postman-token': "8d5daf06-af9e-eb5f-6cf7-c137ac9c9c5e"
        # }
        # response = requests.request(
        #     "GET", url, headers=headers, params=querystring)
        # if response.text != 'null':
        #     latestFinancialData = json.loads(response.text)
        #     if 'ROE' in latestFinancialData and type(latestFinancialData['ROE']) == float:
        #         stock.ROE = latestFinancialData['ROE'] * 100
        #     if 'EPS' in latestFinancialData and type(latestFinancialData['EPS']) == float:
        #         stock.EPS = latestFinancialData['EPS']
        #     if 'MarketCapitalization' in latestFinancialData and type(latestFinancialData['MarketCapitalization']) == float:
        #         stock.MarketCapitalization = latestFinancialData['MarketCapitalization'] / 10**9
        # stock.financial_data = response.text
            stock.save()
            # if not stock.id:
                # return JsonResponse({'data': 'Created failed'})
        return JsonResponse({'data': 'Created successfully'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def stock_detail(request, pk):
    return JsonResponse({'data': 'detail'})


@csrf_exempt
def stock_update(request, pk):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'Symbol' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_symbol = body['Symbol']
        filter_symbols = Stock.objects.filter(Symbol=search_symbol)
        if len(filter_symbols) == 1:
            symbol = filter_symbols[0]
            if 'Volume' in body:
                symbol.Volume = body['Volume']
            if 'Close' in body:
                symbol.Close = body['Close']
            if 'today_capitalization' in body:
                symbol.today_capitalization = body['today_capitalization']
            if 'percentage_change_in_price' in body:
                symbol.percentage_change_in_price = body['percentage_change_in_price']
            symbol.save()
            Volume_min = 0
            RSI_14_max = 1000000
            RSI_14_min = 0
            RSI_14_diff_min = 0
            ROE_min = 0
            EPS_min = 0
            today_capitalization_min = 5000000000
            percentage_change_in_price_min = 0.01
            check_filtered_symbol = Stock.objects.filter(Q(id=symbol.id) & Q(Volume__gt=Volume_min) & Q(
                RSI_14__gt=RSI_14_min) & Q(RSI_14__lt=RSI_14_max) & Q(
                RSI_14_diff__gt=RSI_14_diff_min) & Q(
                    ROE__gt=ROE_min) & Q(
                        EPS__gt=EPS_min) & Q(
                            today_capitalization__gt=today_capitalization_min) & Q(
                                percentage_change_in_price__gt=percentage_change_in_price_min)
            ).order_by('-today_capitalization')
            print(len(check_filtered_symbol) == 0)
            if len(check_filtered_symbol) == 0:
                return JsonResponse({'data': 'Updated successfully'})
            filtered_stocks = Stock.objects.filter(Q(Volume__gt=Volume_min) & Q(
                RSI_14__gt=RSI_14_min) & Q(RSI_14__lt=RSI_14_max) & Q(
                RSI_14_diff__gt=RSI_14_diff_min) & Q(
                    ROE__gt=ROE_min) & Q(
                        EPS__gt=EPS_min) & Q(
                            today_capitalization__gt=today_capitalization_min) & Q(
                                percentage_change_in_price__gt=percentage_change_in_price_min)
            ).order_by('-today_capitalization')
            result = []
            for stock_item in filtered_stocks:
                result.append(get_default_attributes(stock_item))
            return JsonResponse({'data': 'Updated successfully', 'stock': get_default_attributes(symbol), 'stocks': result})
        return JsonResponse({'data': 'Item not found'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def stock_delete(request, pk):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if not 'id' in body:
            return JsonResponse({'data': 'Invalid data'})
        search_id = body['id']
        stocks = Stock.objects.filter(id=search_id).delete()
        if stocks[0] == 1:
            return JsonResponse({'data': 'Deleted successfully'})
        else:
            return JsonResponse({'data': 'Deleted failed'})


@csrf_exempt
def stock_delete_all(request):
    if request.method == 'POST':
        Stock.objects.all().delete()
        return JsonResponse({'data': 'Deleted all stocks successfully'})
    return JsonResponse({'data': 'Deteled all stocks failed'})


@csrf_exempt
def get_quick_filtered_stocks(request):
    filtered_stocks = Stock.objects.filter(Q(Volume__gt=10000) & Q(
        RSI_14__gt=60) & Q(RSI_14__lt=70) & Q(RSI_14_diff__gt=0) & Q(ROE__gt=17) & Q(EPS__gt=3000))
    result = []
    for stock in filtered_stocks:
        result.append(get_default_attributes(stock))
    return JsonResponse({'stocks': result})


@csrf_exempt
def stock_filter(request):
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
        RSI_14_min = -99999999
        RSI_14_diff_min = -99999999
        ROE_min = -99999999
        EPS_min = -99999999
        today_capitalization_min = 0
        percentage_change_in_price_min = -99999999
        Symbol_search = ''
        # Date = '"' + datetime.now().strftime("%Y-%m-%d") + 'T00:00:00Z"'
        # if 'Date' in body:
        #     Date = body['Date']
        last_updated_time = ''
        configs = Config.objects.filter(key='LAST_UPDATED_TIME')
        if len(configs) > 0:
            last_updated_time =  configs[0].value[1:-1]
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
        # print(last_updated_time, today_capitalization_min, percentage_change_in_price_min)
        filtered_stocks = Stock.objects.filter(
            # Q(Volume__gt=Volume_min) & 
            # Q(RSI_14__gt=RSI_14_min) & 
            # Q(RSI_14__lt=RSI_14_max) & 
            # Q(RSI_14_diff__gt=RSI_14_diff_min) & 
            # Q(ROE__gt=ROE_min) & 
            # Q(EPS__gt=EPS_min) & 
            Q(Date=last_updated_time) & 
            Q(today_capitalization__gt=today_capitalization_min) & 
            Q(percentage_change_in_price__gt=percentage_change_in_price_min)
            # Q(Symbol__regex=r'{0}'.format(Symbol_search))
        ).order_by('-today_capitalization')
        
        for stock in filtered_stocks:
            result.append(get_default_attributes(stock))
        return JsonResponse({'stocks': result})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def stock_analyze(request):
    today_capitalization_min = 5000000000
    Close = 3000
    percent = 1.1
    period = 14
    justify = False
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if 'percent' in body:
            percent = float(body['percent'])
        if 'period' in body:
            period = int(body['period'])
        if 'justify' in body:
            justify = True
        filtered_stocks = Stock.objects.filter(Q(Close__gt=Close) & Q(
            today_capitalization__gt=today_capitalization_min))
        if justify == True:
            return_obj = {
                'max_count': 0,
                'percent': 0,
                'period': 0,
                'mapped_result': []
            }
            list_obj = []
            for i in range(5, 10):
                for j in range(105, 110):
                    result = []
                    count = 0
                    for stock in filtered_stocks:
                        result.append(get_analyze_attributes(stock, j/100, i))
                    mapped_result = mapData(result)
                    for k in range(0, len(mapped_result)):
                        count += mapped_result[k]['value']
                    if return_obj['max_count'] < count:
                        return_obj['max_count'] = count
                        return_obj['percent'] = j/100
                        return_obj['period'] = i
                        return_obj['mapped_result'] = mapped_result
                    list_obj.append({
                        'max_count': count,
                        'percent': j/100,
                        'period': i,
                        'mapped_result': mapped_result
                    })
            print(return_obj)
            return JsonResponse({'symbol': return_obj['mapped_result'], 'return_obj': return_obj, 'list_obj': list_obj})
        else:
            result = []
            for stock in filtered_stocks:
                result.append(get_analyze_attributes(stock, percent, period))
            mapped_result = mapData(result)
            return JsonResponse({'symbol': mapped_result})
    return JsonResponse({'data': 'invalid'})


def mapData(data):
    result = {}
    converted_result = []
    for i in range(0, len(data)):
        item = data[i]["result"]
        for j in range(0, len(item)):
            if not item[j] in result:
                result[item[j]] = []
            result[item[j]].append(data[i]["Symbol"])
    keys = list(result)
    keys.sort()
    for k in range(0, len(keys)):
        key = str(keys[k])[0: 10]
        if (re.search("(2016|2017|2018|2019)", key)):
            converted_result.append({
                "name": str(keys[k])[0: 10],
                "data": result[keys[k]],
                "value": len(result[keys[k]])
            })
    return converted_result


@csrf_exempt
def stock_backtest(request):
    if request.method == 'POST':
        all_backtests = []
        body = json.loads(request.body.decode('utf-8'))
        array = []
        for m in range(1, 13):
            index = m * 23 * 16
            item = '[' + date_2017()[index:] + ',' + date_2018()[0:index - 1] + ']'
            array.append(item)
        # print(array)
        for n in range(0, len(array)):
        # for n in range(0, 1):
            date_array = json.loads(array[n])
            # date_array = json.loads(array_test())
            for i in range(3, 30):
                for j in range(0, 10):
                    for k in range(103, 120):
                    # print(i, j)
                        all_backtests.append(backtest(date_array, i, j, k/100))
                        title = array[n][2:22] + '|' + array[n][-22:-2] + 'time_period' + str(i) + 'position_stock' + str(j) + 'percent' + str(k)
                        filtered_posts = Post.objects.filter(title=title)
                        if len(filtered_posts) == 0:
                            post = Post()
                            post.title = title
                            post.content = json.dumps(all_backtests)
                            post.save()
    return JsonResponse({'data': all_backtests[0], 'data1': all_backtests})

def backtest(date_array, time_period, position_stock, percent):
    # percent = 0.05
    result = []
    NAV = 20
    k = 0
    # print(date_array, time_period, position_stock)
    while k < len(date_array) - time_period:
        today_capitalization_min = 0
        percentage_change_in_price_min = 0.01
        filtered_stocks = Stock.objects.filter(
            Q(Date=date_array[k]) &
            Q(today_capitalization__gt=today_capitalization_min) &
            Q(percentage_change_in_price__gt=percentage_change_in_price_min)
            ).order_by('-today_capitalization')
        increment_number = time_period
        # print(filtered_stocks, 433)
        if len(filtered_stocks) > 0:
            stock_obj = filtered_stocks[0]
            if len(filtered_stocks) > position_stock:
                stock_obj = filtered_stocks[position_stock]
            start_obj = stock_obj
            print(437, start_obj)
            m = 3
            end_objs = Stock.objects.filter(
                Q(Date=date_array[k+time_period]) & 
                Q(Symbol=start_obj.Symbol)
            )
            if len(end_objs) > 0:
                end_obj = end_objs[0]
                buy_price = start_obj.Open
                sell_price = end_obj.Close
                while m < time_period:
                    filtered_end_obj = Stock.objects.filter(
                        Q(Date=date_array[k+m]) & 
                        Q(Symbol=start_obj.Symbol)
                    )
                    if len(filtered_end_obj) > 0:
                        end_obj = filtered_end_obj[0]
                        if end_obj.Low <= (1 - percent) * buy_price:
                            sell_price = (1 - percent) * buy_price
                            increment_number = m
                            break
                        if end_obj.High >= (1 + percent) * buy_price:
                            sell_price = (1 + percent) * buy_price
                            increment_number = m
                            break
                    m += 1
                mapped_start_obj = get_default_attributes(start_obj)
                mapped_end_obj = get_default_attributes(end_obj)
                volume = NAV * 1000000 / buy_price
                
                NAV = NAV * sell_price / buy_price
                result.append({
                    'Symbol': stock_obj.Symbol,
                    'start_obj': mapped_start_obj,
                    'end_obj': mapped_end_obj,
                    'buy_price': buy_price,
                    'sell_price': sell_price,
                    'volume': volume,
                    'NAV': NAV
                })
        k += increment_number
    # print(450, result)
    return result

def stock_backtest_results(request):
    posts = Post.objects.filter(title__regex=r'position_stock')
    results = []
    for i in range(0, len(posts)):
        results.append({
            'title': posts[i].title,
            'content': posts[i].content
        })
    return JsonResponse({'data': results})