from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('검색어를 입력하세요:')
url = baseUrl + quote_plus(plusUrl)

# permission error 13
PATH = "/Users/yongsoo/Documents/VSCode/Python/"
dirver = webdriver.Chrome(PATH)
dirver.get(url)

html = dirver.page_source
soup = BeautifulSoup(html)

r = soup.select('.r')

for i in r:
    print(i.select_one('.ellip').text)
    print(i.a.attrs['href'])
    print()

