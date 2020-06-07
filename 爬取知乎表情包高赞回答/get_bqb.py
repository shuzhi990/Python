
import re
import requests
from bs4 import BeautifulSoup as bf
from requests.exceptions import HTTPError
from urllib.request import urlretrieve

#京东搜索的url
#url= 'https://search.jd.com/Search?keyword=%E5%8F%A3%E7%BA%A2&enc=utf-8'
i = 0
links =[]
#模仿火狐浏览器
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}

url = 'https://www.zhihu.com/question/65141944/answer/541829976?utm_source=qq&utm_medium=social&utm_oi=1082569477098602496 '
try:
    res = requests.get(url,timeout = 10,headers=headers)
    res.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
except Timeout:
    print('The request timed out')
else:
    print('Success!')
    obj = bf(res.text,'lxml')
    mes_comments = obj.find_all('img',{'src':re.compile('.jpg')})
    for comment in mes_comments:
        link = comment.get('src')
        links.append(link)
        i+=1
        name = 'dbqb'+str(i)+'.jpg'
        urlretrieve(link, name)