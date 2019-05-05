'''
Gather data in key_list for specified city and in specified time span through web crawler.
'''
import os
import csv
import json
import time
import requests
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')

key_list = ['date','temperature', 'temperature_normal',
            'min_temperature', 'min_temperature_normal', 'min_temperature_record',
            'max_temperature', 'max_temperature_normal', 'max_temperature_record',
            'precip', 'precipnormal', 'preciprecord']


def gather_data(city, date):
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
    data = []
    data.append(str(date))
    for key in key_list[1:]:
        data.append(str(table[key]))
    return data


def generate_csvfile(city, start_date, end_date, filename=""):
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
    with open('data/{}.csv'.format(city), 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(key_list) # column name

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
                    print('Gathering data of year:{}, month:{}.'.format(date[0:4], date[4:6]))
                data = gather_data(city, date)
                writer.writerow(data)
                #print(date)
                #time.sleep(1) # release cache
            except Exception:
                continue

            current_date += timedelta(days=1)
    print('cvs file has generated to {}'.format(file.name))

def date_to_str(current_date):
    year = str(current_date.year)
    month = str(current_date.month)
    day = str(current_date.day)
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    date = year + month + day
    return date



if __name__ == '__main__':
    city = 'KSFO'
    start_date = '20000101'
    end_date = '20190430'
    generate_csvfile(city, start_date, end_date)
