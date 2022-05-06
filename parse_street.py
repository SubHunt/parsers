import requests
from bs4 import BeautifulSoup as bs

BASE_URL = 'https://www.thestreet.com/investing'
#URL = 'https://fincult.info/articles/'
#HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', 'accept': '*/*'}
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.855 Yowser/2.5 Safari/537.36'
headers = {
    'User-Agent': user_agent
}


def parse():
    ses = requests.Session()
    response = ses.get(url=BASE_URL, headers=headers)
    if response.status_code == 200:
        print('OK')
        soup = bs(response.content, 'html.parser')
        items = soup.find_all('div', class_='l-grid--item')
        #items2 = soup.find_all(class_='l-grid--item')
        #print(items2)

        links = []
        for link in items:
            link = link.find('phoenix-super-link').get('href')
            links.append(link)
        print(links)

    else:
        print('Error')

if __name__ == '__main__':
    parse()