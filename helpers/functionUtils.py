import re
from datetime import datetime, timedelta, date
from core.models import Config
from .constants import date_2012, date_2013, date_2014, date_2015, date_2016, date_2017, date_2018, date_2019

def count_trading_times(data, start_time, end_time):
    # print(data)
    array_start_index = []
    array_end_index = []
    for i in range(0, len(data)):
        # if i == 0:
            # print(data[i]['Date'], start_time)
            # print(data[i]['Date'][0:4], start_time[0:4])
        if data[i]['Date'][0:4] == start_time[0:4] and data[i]['Date'][5:7] == start_time[5:7]:
            array_start_index.append(i)
        if data[i]['Date'][0:4] == end_time[0:4] and data[i]['Date'][5:7] == end_time[5:7]:
            array_end_index.append(i)
    print(data[array_start_index[0]]['Date'], data[array_end_index[-1]]['Date'], )
    return {
        'start_obj': data[array_start_index[0]],
        'end_obj': data[array_end_index[-1]],
        'times': array_end_index[-1] - array_start_index[0] + 1
    }

def find_index_array_object(array, key, value):
    i = 0
    while i < len(array):
        if array[i][key] == value:
            return i
        i += 1
    return None

def find_index_array_string(array, string):
    i = 0
    while i < len(array):
        if array[i] == string:
            return i
        i += 1
    return None

def array_test():
    # return '[' + date_2017() + ',' + date_2018() + ']'
    return '[' + date_2018() + ',' + date_2019() + ']'

def range_date_to_update():
    last_updated_time = '"2019-01-02T00:00:00Z"'
    configs = Config.objects.filter(key='LAST_UPDATED_TIME')
    if len(configs) > 0:
        last_updated_time = configs[0].value
    start_time = last_updated_time
    end_time = datetime.now().strftime("%H:%M")
    end_date = datetime.now().strftime("%Y-%m-%d")
    if end_time < '16:00':
        end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    match_end_date = re.search(r'{0}'.format('"' + end_date + 'T00:00:00Z"'), date_2019())
    span_end_date = 0
    if match_end_date is not None:
        span_end_date = match_end_date.span()[1]

    match_start_date = re.search(r'{0}'.format(start_time), date_2019())
    span_start_date = 0
    if match_start_date is not None:
        span_start_date = match_start_date.span()[0]
        
    if last_updated_time == '"2019-01-02T00:00:00Z"':
        return date_2019()[span_start_date:span_end_date]
    return date_2019()[span_start_date + 23:span_end_date]