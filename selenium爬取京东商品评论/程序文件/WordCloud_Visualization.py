import jieba
import re
import pyecharts.options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import pandas as pd
import jieba.analyse as analyse
from collections import Counter


line_comment = []
words = []
#对文本进行初步处理
f = open("K:\学习\comment.txt")
for line2 in f:
    line_comment.append(line2)

punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{} '
string1 = re.sub(r"[%s]+" %punc, "",line_comment[0])
string2 = re.sub(r"[%s]+" %punc, "",line_comment[1])
string0 = string1+string2
string = re.sub(r"[%s]+" %punc, "",string0)



#提取关键词
# for key in analyse.extract_tags(string,50, withWeight=False):
#     print(key)
 
#统计词频
def get_words(string):
    seg_list = jieba.cut(string)
    c = Counter()
    for x in seg_list:
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    for (k,v) in c.most_common(100):
        words.append((k,v))
    
get_words(string)
c = (
    WordCloud()
    .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="评论区内容词云"))
    .render("comment2.html")
)
print(words)
print('已完成任务！')