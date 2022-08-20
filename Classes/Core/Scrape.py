import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
res = requests.get('https://bab.la', headers=headers)
print(res.text)
print(res.status_code)

#find input


def search_site():
