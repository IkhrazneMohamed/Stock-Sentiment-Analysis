import json
import time

import pandas
import requests
import pandas as pd
from secret_keys import nwtime_api_key
import logging

__author__ = 'Gruppe 1'
__doc__ = 'get the article from the archive of the new york times'
__version__ = '1.0.0'

tesla_related_keywords = ['Musk, Elon', 'Tesla Motors Inc', 'Electric and Hybrid Vehicles']


def extract_data_from_api(year, month):
    base_url = 'https://api.nytimes.com/svc/archive/v1/' + str(year) + '/' + str(month) + '.json?api-key={}'
    requested_url = base_url.format(nwtime_api_key)
    print(requested_url)
    time.sleep(10)
    print(time.ctime())
    response = requests.get(url=requested_url)
    print(response)

    if str(response.status_code)[0] == '2':
        logging.info('the request passed successfully : ' + base_url)
        return response.json()
    else:
        print('something went wrong')
        extract_data_from_api(year, month)


def process_data(year, month) -> pandas.DataFrame:
    result = {"news": [], "date": []}
    data = extract_data_from_api(year, month)

    all_articles = data["response"]["docs"]
    len(all_articles)

    for doc in all_articles:
        title = doc["abstract"]
        keywords = doc["keywords"]
        date = doc["pub_date"]

        for keyword in keywords:
            if keyword["value"].title() in tesla_related_keywords:
                result["news"].append(title)
                result['date'].append(date)

    return pd.DataFrame(result)


def save_data_into_csv(data_as_dataframe):
    data_as_dataframe.to_csv('data.csv', sep=',')


if __name__ == '__main__':
    final_data = None

    year_counter = 2017

    while year_counter <= 2022:
        month_counter = 1

        while month_counter <= 12:
            if year_counter == 2022 and month_counter == 12:
                break

            data = process_data(year_counter, month_counter)

            if final_data is None:
                final_data = data
            else:
                final_data.append(data)

            month_counter += 1

        year_counter += 1

    save_data_into_csv(final_data)
