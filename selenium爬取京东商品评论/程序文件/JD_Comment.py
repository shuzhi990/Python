# coding=utf-8
#获取京东口红若干页的评价内容
import re
from time import sleep
from bs4 import BeautifulSoup as bf
from selenium import webdriver
from pandas import Series
print('hello world')
comment = []
real_red = []
#爬虫部分
html_one="https://item.jd.com/3426153.html#comment"
driver=webdriver.Firefox()
driver.get(html_one)
sleep(5)
for i in range(75):
    sleep(2)
    page=bf(driver.page_source,'html5lib')
    com = page.find('div',{'id':"comment-0"})
    #另一种格式
    # mes = com.find_all("span",{"class": 'text'})
    mes = com.find_all("p",{"class": 'comment-con'})
    for text in mes:
        #另一种格式
        #print(color.get_text())
        comment.append(text.get_text())
        
    #自动翻页
    a = driver.find_element_by_link_text('下一页')
    a.click()
driver.close()

with open("douban.txt","w") as f:
    for i in range(len(comment)):
        f.write(comment[i])