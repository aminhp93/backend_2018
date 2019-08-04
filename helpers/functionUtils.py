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