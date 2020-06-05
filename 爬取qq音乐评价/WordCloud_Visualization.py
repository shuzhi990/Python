#jieba分词并绘制词云
import jieba
import re
import pyecharts.options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import pandas as pd
import jieba.analyse as analyse
from collections import Counter

line_comment = ' '
words = []
#对文本进行初步处理
f = open("K:\爬虫实例\爬取qq音乐评价\qq_Music_Comment.txt",encoding='UTF-8')
for line2 in f:
    line_comment+=line2

punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{} '
string0 = re.sub(r"[%s]+" %punc, "",line_comment)
string = re.sub(r"[%s]+" %punc, "",string0)
 
#统计词频
def get_words(string):
    seg_list = jieba.cut(string)
    c = Counter()
    for x in seg_list:
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    for (k,v) in c.most_common(200):
        words.append((k,v))
    
get_words(string)
c = (
    WordCloud()
    .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="「入海」评论高频词云"))
    .render("K:\爬虫实例\爬取qq音乐评价\WordCloud_Visualization.html")
)
print(words)
print('已完成任务！')