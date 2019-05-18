'''
Wrapper function to generate cleand data
'''
from data_crawler import *
from data_cleaner import *
from global_variables import *


if __name__ == '__main__':
    # generate cleaned data
    '''
    start_date = '19900101'
    end_date = '20190430'
    for city in list(city_code_refer.values()):
        fname = city + '.csv'
        generate_csvfile(city, start_date, end_date, filename=fname)
        print('---------------data collected---------------')
        clean_data('data/{}.csv'.format(city))
        print('----------------data cleaned----------------')
    '''