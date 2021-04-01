from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from  bs4 import BeautifulSoup
import json
import re

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요:')

url = baseUrl + quote_plus(plusUrl)

print(url)  

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

print(len(soup.findAll('script')))
# print('==============')
# img = soup.find_all(class_='_img')
# 정규식으로 패턴 생성
pattern = re.compile(r'controller.start\(\[(.*?)\]\)', re.MULTILINE | re.DOTALL)
# 패턴이 적용된 스크립트 가져온다
script = soup.find("script", text=pattern)
# print(script)
print('================')

if script:
    # 스크립트 내용을 문자열로 전환후 패텐이 맞는 부분만 가져온다
    jsStr = pattern.search(str(script.contents[0])).group(0).replace("controller.start([", "[").replace("])", "]");
    # print(jsStr)
    json_data = json.loads(jsStr)
    print(len(json_data))
    # imgs = []
    n = 1
    for el in json_data :
        # print(el)
        # imgs.append(el.get('originalUrl'))
        if(n == 10) : 
            break;
        with urlopen(unquote_plus(el.get('originalUrl'))) as f:
            with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        n += 1

print('다운로드 완료')
