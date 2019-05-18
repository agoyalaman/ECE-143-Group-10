'''
Gather data in key_list for specified city and in specified time span through web crawler.
'''
import os
import csv
import json
import time
import requests
import warnings
import pandas as pd
from global_variables import *
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')


def gather_data(city, date):
    '''
    gather the data table form website for a specific city and date
    :param city: str, city code
    :param date: str, eg:20180101
    :return: data table on the websit
    '''
    # Get data table
    session = requests.session()
    response = session.get('https://api-ak.wunderground.com/api/d8585d80376a429e/history_{}/lang:EN/units:english/bestfct:1/v:2.0/q/'
              '{}.json?showObs=0&ttl=120'.format(date, city), headers=None, verify=False)
    dictionary = json.loads(response.text)
    table = dictionary['history']['days'][0]['summary']
    #print(dictionary['history']['days'][0]['summary'].keys())
    # Gather data
    data = format_data(table, date, key_list)
    return data


def format_data(table, date, key_list):
    '''

    :param table: data table
    :param date: str
    :param key_list: the key name of data want to be gather
    :return: formatted data list
    '''
    data = list()
    data.append(str(date))
    for key in all_key_list[1:]:
        data.append(str(table[key]))
    return data


def generate_csvfile(city, start_date, end_date, filename=""):
    '''
    gather data from start date to end date
    :param city: city code
    :param start_date: start date
    :param end_date: end data
    :param filename: specified filename under path'data/'
    :return:
    '''
    # Validation
    assert isinstance(city, str), "city is not valid"
    assert isinstance(start_date, str) and len(start_date) == 8, "date is not valid"
    assert isinstance(end_date, str) and len(end_date) == 8, "date is not valid"
    assert filename == "" or filename [-4:] == ".csv"
    # Initialization
    if not os.path.exists('data/'):
        os.makedirs('data/')
    if filename == "":
        filename = 'data/{}_{}_{}.csv'.format(city, start_date, end_date)
    current_date = datetime(year=int(start_date[0:4]), month=int(start_date[4:6]), day=int(start_date[6:]))
    end_date = datetime(year=int(end_date[0:4]), month=int(end_date[4:6]), day=int(end_date[6:]))
    last_time = None
    with open('data/'+filename, 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(all_key_list) # column name

        while current_date != end_date + timedelta(days=1):

            try:
                date = date_to_str(current_date)

                if date[6:] == '01':
                    current_time = datetime.now()
                    if last_time == None:
                        last_time = current_time
                    else:
                        print('time spent: {}s'.format((current_time - last_time).seconds))
                        last_time = current_time
                    print('Gathering data of {} in year:{}, month:{}.'.format(city, date[0:4], date[4:6]))
                data = gather_data(city, date)
                writer.writerow(data)
                #print(date)
                #time.sleep(1) # release cache
            except Exception:
                continue

            current_date += timedelta(days=1)
    print('cvs file has generated to {}'.format(file.name))


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


def print_info(city='KSAN', date='19900101',key_step=5):
    '''
    helper function, show data information
    :param city: city code
    :param date: 8 digit date string
    :param key_step: the number of keys printed out every row
    :return:
    '''
    session = requests.session()
    response = session.get(
        'https://api-ak.wunderground.com/api/d8585d80376a429e/history_{}/lang:EN/units:english/bestfct:1/v:2.0/q/'
        '{}.json?showObs=0&ttl=120'.format(date, city), headers=None, verify=False)
    dictionary = json.loads(response.text)
    table = dictionary['history']['days'][0]['summary']
    table['date'] = date
    print('The table  is:\n', pd.Series(table))
    all_key_list = list(table.keys())
    print('The list of table\'s key is:')
    if key_step >= 1:
        for i in range(len(all_key_list)):
            if i*key_step < len(all_key_list):
                print(all_key_list[i*key_step:(i+1)*key_step])


if __name__ == '__main__':
    # info
    print_info()
    # gather data
    '''
    start_date = '19900101'
    end_date = '20190430'
    for city in list(city_code_refer.values()):
        fname = city + '.csv'
        generate_csvfile(city, start_date, end_date, filename=fname)
        print('-------------------------------------------')
    '''
    pass


