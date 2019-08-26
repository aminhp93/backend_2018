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
    print(data[array_start_index[0]]['Date'],
          data[array_end_index[-1]]['Date'], )
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
    # return '[' + date_2016()[23:-1] + ',' + date_2017()[0:22] + ']'
    # return '[' + date_2016()[23 + 23:-1] + ',' + date_2017()[0:22 + 23] + ']'
    return '[' + date_2017()[2300:] + ',' + date_2018()[0:2299] + ']'


def range_date_to_update():
    today_date = datetime.now().strftime("%Y-%m-%d")
    weekday = datetime.now().strftime("%a")
    if weekday == 'Sat':
        today_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    elif weekday == 'Sun':
        today_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    search_today_date = re.search(r'{0}'.format(today_date), date_2019())
    if search_today_date == None:
        return ''
    end_index = search_today_date.span()[0]

    last_updated_time = get_last_updated_time()
    if last_updated_time is None:
        last_updated_time = '2019-01-02'
    last_updated_time = '"' + last_updated_time + 'T00:00:00Z"'
    start_time = last_updated_time
    match_start_date = re.search(r'{0}'.format(start_time), date_2019())
    start_index = 0
    if match_start_date is not None:
        start_index = match_start_date.span()[1]
    # print(start_index, end_index)
    return date_2019()[start_index:end_index + 21]

def get_last_updated_time():
    today_date = datetime.now().strftime("%Y-%m-%d")
    today_hour = (datetime.now() - timedelta(hours=17)).strftime("%H")
    configs = Config.objects.filter(key='LAST_UPDATED_TIME')
    last_updated_time = None
    if configs:
        last_updated_time = configs[0].value[1:11]
    if today_date == last_updated_time:
        if today_hour < '16' and today_hour > '00':
            last_updated_time = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    return last_updated_time