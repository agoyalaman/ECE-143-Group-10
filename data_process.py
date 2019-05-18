'''
Data process funtcions
'''
import os
import numpy as np
import pandas as pd
import matplotlib as plt
from global_variables import *


def get_city_fname(city):
    return 'data/{}_cleaned.csv'.format(city)


def count_icon_days(selected_data):
    icon_count_series = selected_data.groupby(by='icon').size()
    icon_count_df = pd.DataFrame(icon_count_series, columns=['days']).sort_values(by='days', ascending=False)
    return icon_count_df


def get_temp_describe(selected_data):
    return pd.DataFrame(selected_data['temperature'].describe())


def get_temp_minmax(selected_data):
    # Max temp
    max_temp = selected_data['max_temperature'].max()
    max_temp_dates = selected_data[selected_data.max_temperature.astype(float) == float(max_temp)].index.tolist()
    # Min temp
    min_temp = selected_data['min_temperature'].min()
    min_temp_dates = selected_data[selected_data.min_temperature.astype(float) == float(min_temp)].index.tolist()
    # Average temp
    max_avg_temp = selected_data['temperature'].max()
    max_avg_temp_dates = selected_data[selected_data.temperature.astype(float) == float(max_avg_temp)].index.tolist()
    min_avg_temp = selected_data['temperature'].min()
    min_avg_temp_dates = selected_data[selected_data.temperature.astype(float) == float(min_avg_temp)].index.tolist()
    temp = dict([('max_temp', max_temp), ('max_temp_dates', max_temp_dates),
                 ('min_temp', min_temp), ('min_temp_dates', min_temp_dates),
                 ('max_avg_temp', max_avg_temp), ('max_avg_temp_dates', max_avg_temp_dates),
                 ('min_avg_temp', min_avg_temp), ('min_avg_temp_dates', min_avg_temp_dates)])
    return temp


def get_precip_describe(selected_data):
    return pd.DataFrame(selected_data['precip'].describe())


def get_precip_minmax(selected_data):
    max_precip = selected_data['precip'].max()
    max_precip_dates = selected_data[selected_data.precip.astype(float) == float(max_precip)].index.tolist()
    min_precip = selected_data['precip'].min()
    if float(min_precip) == 0.0:
        min_precip_dates = []
    else:
        min_precip_dates = selected_data[selected_data.precip.astype(float) == float(min_precip)].index.tolist()

    prec = dict([('max_precip', max_precip), ('max_precip_dates', max_precip_dates),
                 ('min_precip', min_precip), ('min_precip_dates', min_precip_dates)])
    return prec


def process_weather_info(city, start_date, end_date, output=0):
    # Validation
    assert isinstance(city, str), 'city is not valid'
    fname = get_city_fname(city)
    assert os.path.exists(fname), 'file does not exist'
    origin_data = pd.DataFrame(pd.read_csv(fname))
    origin_data.set_index(["date"], inplace=True)
    selected_data = origin_data.loc[start_date:end_date]
    # Count wether
    icon_count = count_icon_days(selected_data)
    # Temperature info
    temperature_description = get_temp_describe(selected_data)
    temperature_minmax = get_temp_minmax(selected_data)
    # Precipitation info
    precipitation_description = get_precip_describe(selected_data)
    precipitation_minmax = get_precip_minmax(selected_data)
    if output == 1:
        print('The information of {} from {} to {} are shown below:'.format(city, start_date, end_date))
        print('---------WETHER PART---------')
        print('icon_count:\n',icon_count)
        print('-------TEMPERAURE PART-------')
        print('temperature_description:\n',temperature_description)
        print('temperature_minmax:\n',temperature_minmax)
        print('-----PERCIPITATION PART------')
        print('precipitation_description:\n',precipitation_description)
        print('precipitation_minmax:\n',precipitation_minmax)

    return icon_count, temperature_description, temperature_minmax, precipitation_description, precipitation_minmax

if __name__ == '__main__':
    city = 'KSAN'
    start_date = '20100101'
    end_date = '20101231'
    process_weather_info(city, start_date, end_date, output=1)