'''
Some helper function to get data's info
'''
import os
import calendar
import pandas as pd
from datetime import datetime, timedelta
from global_variables import *


# Process the weather icon
def get_weather_info(city, start_date, end_date, output=True):
    selected_data = select_data(city, start_date, end_date)
    weather_info = selected_data.groupby(by='icon').size()
    weather_info = pd.DataFrame(weather_info, columns=['days']).sort_values(by='days', ascending=False)
    weather_info['percentage'] = weather_info.eval('days / days.sum()')
    if output:
        print('The weather information of {} during {}-{} :'.format(code_city_refer[city], start_date, end_date))
        print('Total days: {}'.format(selected_data['icon'].count()))
        print(weather_info)
    return weather_info


# Process the temperature &  the precipitation
def get_info(city, start_date, end_date, info_type='temperature', output=True):
    if info_type == 'weather':
        return get_weather_info(city, start_date, end_date, output)
    else:
        column = get_column(info_type)
        selected_data = select_data(city, start_date, end_date)
        max = selected_data[column].max()
        max_dates = selected_data[selected_data.temperature.astype(float) == float(max)].index.tolist()
        min = selected_data[column].min()
        if info_type=='precipitation' and min == 0.0:
            min_dates = []
        else:
            min_dates = selected_data[selected_data.temperature.astype(float) == float(min)].index.tolist()
        temp_info = dict([('mean',selected_data[column].mean()),
                          ('std', selected_data[column].std()),
                          ('count', selected_data[column].count()),
                          ('max', max), ('max_dates', max_dates),
                          ('min', min), ('min_dates', min_dates)])
        if output:
            print('The {} information of {} during {}-{} :'.format(info_type, code_city_refer[city], start_date, end_date))
            print(temp_info)
        return temp_info


# Helper function
def get_city_fname(city):
    '''
    Generate the file name of a specific city
    :param city: city code
    :return: cleaned data file name
    '''
    assert isinstance(city, str) and city in city_code_refer.values(), 'city code invalid'
    return 'data/{}_cleaned.csv'.format(city)


def select_data(city, start_date, end_date):
    '''
    Get city's data in specified time period
    :param city: city code
    :param start_date:
    :param end_date:
    :return: pd.DataFrame with date as index
    '''
    fname = get_city_fname(city)
    assert os.path.exists(fname), 'file does not exist'
    origin_data = pd.DataFrame(pd.read_csv(fname))
    origin_data.set_index(["date"], inplace=True)
    assert int(start_date) in origin_data.index.tolist(), 'Input start date is invalid'
    assert int(end_date) in origin_data.index.tolist(), 'Input end date is invalid'
    selected_data = origin_data.loc[start_date:end_date]

    return selected_data


def get_column(info_type):
    column_map = dict([('weather','weather'),
                       ('temperature','temperature'),
                       ('precipitation','precip'),
                       ('highest temperature','max_temperature'),
                       ('lowest temperature','min_temperature')])
    assert info_type in column_map.keys(), 'The info_type is invalid'
    return column_map[info_type]


def date_to_str(current_date):
    '''
    change date object to 8 digit date string
    :param current_date: date object
    :return: 8 digit date string
    '''
    year = str(current_date.year)
    month = str(current_date.month)
    day = str(current_date.day)
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    date = year + month + day
    return date


def get_monthly_start_end(year=1990, month=1):
    assert isinstance(year, int) and 1990 <= year <= 2019, 'Input year is invalid'
    assert isinstance(month, int) and 1 <= month <= 12, 'Input month is invalid'
    if year == 2019:
        assert 1 <= month <= 4, 'Input month is invalid'
    month_range = calendar.monthrange(year=year, month=month)
    start_date = date_to_str(datetime(year=year, month=month, day=1))
    end_date = date_to_str(datetime(year=year, month=month, day=month_range[1]))
    #print(start_date, end_date)
    return start_date, end_date


def get_yearly_start_end(year=1990):
    assert isinstance(year, int) and 1990 <= year <= 2019, 'Input year is invalid'
    start_date = str(year) + '0101'
    if year == 2019:
        end_date = '20190430'
    return start_date, end_date


if __name__ == '__main__':
    city = 'KSAN'
    start_date = '20100101'
    end_date = '20101231'
    get_info(city, start_date, end_date, info_type='weather')
    start, end = get_monthly_start_end(year=1990, month=2)
    print(start, end)