from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

__doc__ = 'extract news header from reuters using selenium'


def register_driver():
    my_driver = webdriver.Chrome(r'C:\driver\chromedriver')
    my_driver.implicitly_wait(1)

    my_driver.maximize_window()

    return my_driver


def extract_data():
    data = {
        "category": [],
        "title": [],
        "date": [],
        "url_to_article": []
    }

    start_url = 'https://www.reuters.com/site-search/?query=tesla'

    pages_number = 0

    while pages_number <= 2942:

        url = "https://www.reuters.com/site-search/?query=tesla&offset={}".format(str(pages_number))

        driver = register_driver()
        try:
            driver.get(url)
            file.write(url + '\n')
        except Exception:
            print('no page exist anymore', Exception)
        try:
            go_per_page = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div['
                                                    '3]/span[1]').text.split(' ')
            counter = 1
            while counter <= (int(go_per_page[2]) - int(go_per_page[0]) + 1):

                header_selector = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[{}]".format(
                    str(counter))
                url_to_article = '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[{}]/div[' \
                                 '1]/div[1]/a[1]/span[1]'.format(str(counter))
                try:
                    news_header_info_list = driver.find_element(By.XPATH, header_selector).text
                    url_to_article = driver.find_element(By.XPATH, url_to_article).get_attribute('href')
                    ## split the header
                    news_header_info_list = news_header_info_list.split('\n')
                    data['category'].append(news_header_info_list[0])
                    data['title'].append(news_header_info_list[1])
                    data['date'].append(news_header_info_list[-1])
                    data['url_to_article'].append(url_to_article)
                except Exception:
                    print(Exception)

                counter += 1

            driver.close()
        except Exception:
            print(url)

        pages_number = pages_number + counter

    return data


def prepross_data():

    df = pd.DataFrame(extract_data())

    df.to_csv('scraped_data.csv', sep=',')

    return df


if __name__ == "__main__":
    file = open('save.txt', "a", encoding='utf-8')
    log_file = open('text.txt', 'a', encoding='utf-8')

    prepross_data()

    file.close()
    log_file.close()
