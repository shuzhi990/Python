from selenium import webdriver
from bs4 import BeautifulSoup as bf
import time
import re

word = []
url = 'https://twitter.com/search?q=(from%3ArealDonaldTrump)%20until%3A2020-05-01%20since%3A2020-01-01%20-filter%3Areplies&src=typed_query&f=live'
#创建一个浏览器对象
driver = webdriver.Chrome('k:\学习\chromedriver.exe')
#获取网页
driver.get(url)
#等待加载
time.sleep(5)
def gundong(n):
    driver.execute_script("window.scrollBy(0,"+str(n)+")")
    time.sleep(7)

def get_twitter():
    #读取html文件
    page=bf(driver.page_source,'html5lib')
    #搜索目标信息
    mu_mes = page.find('div',{'style':re.compile('position: relative; min-height: ')})
    mes_links = mu_mes.find_all('div',{'lang':"en"})
    #输出
    for mes in mes_links:
        word.append(mes.span.get_text())

for i in range(1,50):
    n = i*1000
    gundong(n)
    get_twitter()
    print(i)
#关闭浏览器
#driver.close()

with open("twitter2.txt","w") as f:
    for i in range(len(word)):
        f.write(word[i])