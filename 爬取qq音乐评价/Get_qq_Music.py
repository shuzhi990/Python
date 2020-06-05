#爬取时间和评价文本
import json
import time
import datetime
import pandas as pd
import requests

pinglun,time_data = [],[]
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}

def make_url(i):
    url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=265408076&cmd=8&needmusiccrit=0&pagenum='+str(i)+'&pagesize=25'
    return url

def get_page(pages):
    for i in range(pages):
        print("[INFO]正在爬取第%d页"%(i+1))
        url = make_url(i)
        req = requests.get(url,headers = headers)
        #将获取到的二进制级数据转为字符串
        html = str(req.content,'UTF-8')
        data = json.loads(html)
        mes_link = data['comment']['commentlist']
        for mes in mes_link:
            pinglun.append(mes['rootcommentcontent'].replace('\n','').replace('[/em]','').replace('[em]','').replace('e400',''))
            time_data.append(mes['time'])

def Write_Comment():
    with open('爬虫实例\爬取网易云评价\qq_Music_Comment.txt','a',encoding='UTF-8') as f:
        for i in range(len(pinglun)):
            string = pinglun[i].split('\n')
            for i in string:
                i = i.replace('该评论已被删除','')
                f.writelines(i)
                f.write('\n')

def Write_Time():
    with open('爬虫实例\爬取网易云评价\qq_Music_Time.txt','a',encoding='UTF-8') as f:
        for i in range(len(time_data)):
            string = str(time_data[i])
            f.writelines(string)
            f.write('\n')

if __name__ == "__main__":
    start = time.time()
    get_page(966)
    Write_Comment()
    Write_Time()
    print("[INFO]爬取结束")
    Space_Time0 = int(time.time()-start)
    print("[INFO]程序共耗时%d秒"%Space_Time0)
