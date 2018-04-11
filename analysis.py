# -*- coding: utf-8 -*-

import csv
from datetime import datetime
from pprint import pprint


def print_first_point(filename):
    # 输出城市名以供参考
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))

    with open(filename, 'r') as f_in:
        ## 待办：用 csv 库来设置一个 DictReader 对象。##
        ## 见 https://docs.python.org/3/library/csv.html           ##
        trip_reader = csv.DictReader(f_in)

        ## 待办：对 DictReader 对象使用函数     ##
        ## 从而读取数据文件的第一条骑行记录并将其存储为一个变量     ##
        ## 见 https://docs.python.org/3/library/csv.html#reader-objects ##
        #title = next(trip_reader)
        first_trip = next(trip_reader)

        ## 待办：用 pprint 库来输出第一条骑行记录。 ##
        ## 见 https://docs.python.org/3/library/pprint.html     ##
        pprint(first_trip)

    # 输出城市名和第一条骑行记录以备测试
    return (city, first_trip)


# 各城市的文件列表
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv', ]

# 输出各文件的第一条骑行记录，并将其储存在字典中
example_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip
print(example_trips)
print(example_trips['NYC'])

data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv', ]


def duration_in_mins(datum, city):
    """
    将一个字典作为输入，该字典需包含一条骑行记录（数据）
    及记录城市（城市）的信息，返回该骑行的时长，使该时长以分钟为单位。

    记住，华盛顿特区是以毫秒作为计量单位的，而芝加哥和纽约市则
    以秒数作为单位。

    提示：csv 模块会将所有数据读取为字符串，包括数值，
    所以转换单位时，你需要用一个函数来将字符串转换为合适的数值类型。
    见 https://docs.python.org/3/library/functions.html
    """

    # 请在此处写出代码
    if city == 'NYC':
        duration = float(datum['tripduration']) / 60
    elif city =='Chicago':
        duration = float(datum['tripduration']) / 60
    else:
        duration = float(datum['Duration (ms)']) / 60000
    return duration


# 测试代码是否奏效，若所有断言都没问题，则不应有输出出现。
# 至于字典 `example_trips`
# 则是在你输出每个数据源文件的第一条骑行数据时生成的。
"""
tests = {'NYC': 13.9833,
         'Chicago': 15.4333,
         'Washington': 7.1231}

for city in tests:
    assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001
    #print(duration_in_mins(example_trips[city], city))
"""

def time_of_trip(datum, city):
    """
    将一个字典作为输入，该字典需包含一条骑行记录（数据）
    及记录城市（城市）的信息，返回该骑行进行的月份、小时及周几这三个值。


    记住，纽约市以秒为单位，华盛顿特区和芝加哥则不然。

    提示：你需要用 datetime 模块来将原始日期字符串解析为
    方便提取目的信息的格式。
    见 https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """

    # 请在此处写出代码
    if city == 'NYC':
        time = datum['starttime']
        date = datetime.strptime(time, "%m/%d/%Y %H:%M:%S")
        day_of_week = date.strftime('%A')
        month = int(date.strftime('%m'))
        hour = int(date.strftime('%H'))
    elif city == 'Chicago':
        time = datum['starttime']
        date = datetime.strptime(time, "%m/%d/%Y %H:%M")
        day_of_week = date.strftime('%A')
        month = int(date.strftime('%m'))
        hour = int(date.strftime('%H'))
    else:
        time = datum['Start date']
        date = datetime.strptime(time, "%m/%d/%Y %H:%M")
        day_of_week = date.strftime('%A')
        month = int(date.strftime('%m'))
        hour = int(date.strftime('%H'))

    return (month, hour, day_of_week)

# 测试代码是否奏效，若所有断言都没问题，则不应有输出出现。
# 至于字典 `example_trips`
# 则是在你输出每个数据源文件的第一条骑行数据时生成的。

tests = {'NYC': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}

for city in tests:
    print(time_of_trip(example_trips[city], city))
    assert time_of_trip(example_trips[city], city) == tests[city]


def type_of_user(datum, city):
    """
    将一个字典作为输入，该字典需包含一条骑行记录（数据）
    及记录城市（城市）的信息，返回进行该骑行的系统用户类型。


    记住，华盛顿特区的类名与芝加哥和纽约市的不同。

    用户类型： 共享单车系统的注册用户可能与临时用户有不同的使用模式。
    华盛顿特区将其用户分为两种：‘注册用户’ ——这类用户买了较长时期的会员，如年度会员或月度会员；
    ‘临时用户’——这类用户所购买的骑行时间较短，如只有 24 小时或 3 天。纽约市和芝加哥的数据则用
     ‘会员’ 和 ‘散客’ 来区分这两者。为了保证数据的一致性，你需要修改华盛顿特区的标签，使其与另外两座城市的标签相同。

    """

    # 请在此处写出代码
    if city == 'NYC':
        user_type = datum['usertype']
    elif city =='Chicago':
        user_type = datum['usertype']
    else:
        was_tpye = datum['Member Type']
        if was_tpye == 'Registered':
            user_type = 'Subscriber'
        else:
            user_type = 'Customer'

    return user_type


# 测试代码是否奏效，若所有断言都没问题，则不应有输出出现。
# 至于字典 `example_trips`
# 则是在你输出每个数据源文件的第一条骑行数据时生成的。
"""
tests = {'NYC': 'Customer',
         'Chicago': 'Subscriber',
         'Washington': 'Subscriber'}

for city in tests:
    #print(type_of_user(example_trips[city], city))
    assert type_of_user(example_trips[city], city) == tests[city]
"""

def condense_data(in_file, out_file, city):
    """
    本函数会从指定的输入文件中提取全部数据
    并在指定的输出文件中写出浓缩数据。
    城市参数决定输入文件的解析方式。

    提示：参考下框以明确参数结构！
    """

    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        # 设置 csv DictWriter 对象——该对象需将第一列列名
        # 作为 "fieldnames" 参数
        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']
        trip_writer = csv.DictWriter(f_out, fieldnames=out_colnames)
        trip_writer.writeheader()

        ## 待办：设置 csv DictReader 对象##
        trip_reader = csv.DictReader(f_in)

        # 收集并处理每行的数据
        for row in trip_reader:
            # 设置一个字典来存储清理和修剪后的数据点的值
            new_point = {}

            ## 待办：使用辅助函数来从原始数据字典中获取清理数据##
            new_point['duration'] = duration_in_mins(row, city)
            new_point['month'] = time_of_trip(row, city)[0]
            new_point['hour'] = time_of_trip(row, city)[1]
            new_point['day_of_week'] = time_of_trip(row, city)[2]
            new_point['user_type'] = type_of_user(row, city)

            ## 注意字典 new_point 的关键词应与 ##
            ## 上述 DictWriter 对象设置的列名一致。        ##

            ## 待办：在输出文件中写出处理后的信息。##
            ## 见 https://docs.python.org/3/library/csv.html#writer-objects ##
            trip_writer.writerow(new_point)

city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv', 'out_file': './data/Washington-2016-Summary.csv'},
            'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv', 'out_file': './data/Chicago-2016-Summary.csv'},
            'NYC': {'in_file': './data/NYC-CitiBike-2016.csv', 'out_file': './data/NYC-2016-Summary.csv'}}

for city, filenames in city_info.items():
    condense_data(filenames['in_file'], filenames['out_file'], city)
    print_first_point(filenames['out_file'])


def number_of_trips(filename):
    """
    本函数会读取一个骑行数据文件，分别报告
    会员、散客和所有系统用户的骑行次数。
    """
    with open(filename, 'r') as f_in:
        # 设置 csv reader 对象
        reader = csv.DictReader(f_in)

        # 初始化计数变量
        n_subscribers = 0
        n_customers = 0

        # 计算骑行类型
        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
            else:
                n_customers += 1

        # 统计骑行总次数
        n_total = n_subscribers + n_customers

        # 将结果作为数组返回出来
        return (n_subscribers, n_customers, n_total)

data_file = './data/Chicago-2016-Summary.csv'
print(number_of_trips(data_file))