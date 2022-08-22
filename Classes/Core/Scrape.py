from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup

def search_PolishEng(phrase):
    #Headers to pass verification tests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    
    baseURL = "https://en.bab.la/dictionary/polish-english/"
    searchURL = baseURL + phrase

    page = requests.get(searchURL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    uls = soup.find("ul", {"class", "sense-group-results"})

    lis = uls.find_all("li")
    items = []

    for element in lis:
            a = element.find_all("a")
            for item in a:
                items.append(item.text.strip())
    
    items.pop(0)
    return items

search_PolishEng("dzień")
