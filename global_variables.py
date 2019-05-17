all_key_list = ['date', 'temperature', 'dewpoint', 'pressure', 'wind_speed', 'wind_dir',
                'wind_dir_degrees', 'visibility', 'humidity', 'max_temperature', 'min_temperature',
                'temperature_normal', 'min_temperature_normal', 'max_temperature_normal', 'min_temperature_record',
                'max_temperature_record', 'min_temperature_record_year', 'max_temperature_record_year', 'max_humidity',
                'min_humidity', 'max_dewpoint', 'min_dewpoint', 'max_pressure', 'min_pressure', 'max_wind_speed',
                'min_wind_speed', 'max_visibility', 'min_visibility', 'fog', 'hail', 'snow', 'rain', 'thunder',
                'tornado', 'snowfall', 'monthtodatesnowfall', 'since1julsnowfall', 'snowdepth', 'precip',
                'preciprecord', 'preciprecordyear', 'precipnormal', 'since1janprecipitation',
                'since1janprecipitationnormal', 'monthtodateprecipitation', 'monthtodateprecipitationnormal',
                'precipsource', 'gdegreedays', 'heatingdegreedays', 'coolingdegreedays', 'heatingdegreedaysnormal',
                'monthtodateheatingdegreedays', 'monthtodateheatingdegreedaysnormal', 'since1sepheatingdegreedays',
                'since1sepheatingdegreedaysnormal', 'since1julheatingdegreedays', 'since1julheatingdegreedaysnormal',
                'coolingdegreedaysnormal', 'monthtodatecoolingdegreedays', 'monthtodatecoolingdegreedaysnormal',
                'since1sepcoolingdegreedays', 'since1sepcoolingdegreedaysnormal', 'since1jancoolingdegreedays',
                'since1jancoolingdegreedaysnormal', 'avgoktas', 'icon']

key_list = ['date','temperature', 'temperature_normal',
            'min_temperature', 'min_temperature_normal', 'min_temperature_record',
            'max_temperature', 'max_temperature_normal', 'max_temperature_record',
            'precip', 'precipnormal', 'preciprecord']

new_key_list = ['date','temperature', 'min_temperature', 'max_temperature', 'min_temperature_record', 'max_temperature_record',
            'precip', 'preciprecord']


city_code_refer = {'Seattle':'KSEA',
                   'San Francisco':'KSFO',
                   'Los Angeles':'KBUR',
                   'San Diego':'KSAN',
                   'Houston':'KHOU',
                   'Boston':'KBOS',
                   'New York City':'KLGA',
                   'Washington DC':'KDCA'}