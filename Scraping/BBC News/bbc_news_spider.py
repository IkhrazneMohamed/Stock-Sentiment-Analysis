from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

__doc__ = 'extract news header from BBC news using selenium'


def register_driver():
    my_driver = webdriver.Chrome(r'C:\driver\chromedriver')
    my_driver.implicitly_wait(20)
    my_driver.maximize_window()

    return my_driver


def extract_news():
    data = {
        'news': [],
        'date': [],
        "category": []
    }
    for counter in range(1, 30):
        url = 'https://www.bbc.co.uk/search?q=tesla&d=news_gnl&page={}'.format(str(counter))
        driver = register_driver()
        try:
            driver.get(url)
            print(url)
        except Exception:
            print('something went wrong !')

        for i in range(1, 11):
            xpath = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[3]/div[1]/div[1]/ul[1]/li[{}'\
                    ']/div[1]/div[1]/div[1]'.format(str(i))

            container_element = driver.find_element(By.XPATH, xpath).text.split('\n')
            data['news'].append(' '.join([container_element[0], container_element[1]]))
            data['date'].append(container_element[3])
            data['category'].append(container_element[-1])

        driver.close()

    return data


if __name__ == '__main__':
    data = extract_news()

    df = pd.DataFrame(data)

    df.to_csv('data.csv', sep=',')

