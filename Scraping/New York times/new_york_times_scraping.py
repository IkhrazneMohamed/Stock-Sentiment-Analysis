import requests
import pandas as pd
from secret_keys import nwtime_api_key
import logging

__author__ = 'Gruppe 1'
__doc__ = 'get the article from the archive of the new york times'
__version__ = '1.0.0'


def extract_data_from_api(year, month):
    base_url = 'https://api.nytimes.com/svc/archive/v1/' + str(year) + '/' + str(month) + '.json?api-key={}'
    requested_url = base_url.format(nwtime_api_key)

    response = requests.get(url=requested_url)

    if str(response.status_code)[0] == '2':
        logging.info('the request passed successfully : ' + base_url)
        return response.json()
    else:
        print('something went wrong')
        extract_data_from_api(year, month)


def process_data(year, month):
    data = extract_data_from_api(year, month)
    
    ## todo extract articels and check if the article have the requiered keywords

    pass


def save_data_into_csv(data_as_dict):
    df = pd.DataFrame(data_as_dict)

    df.to_csv(r'scraped_data.csv', sep=',')

    return df


if __name__ == '__main__':
    year = 2019
    month = 1
    ## todo year should be between 2017 and 2022
    process_data()
