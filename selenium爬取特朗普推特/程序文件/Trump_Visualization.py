import imageio
import matplotlib.pyplot as plt
import nltk
import pyecharts.options as opts
import wordcloud
from nltk.corpus import stopwords
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

#读取数据
text = []
f = open('K:/学习/twitter.txt')
for line in f:
    text.append(line)
text = str(text)

d_words = nltk.word_tokenize(text)
#停用词
stop = stopwords.words('english')

#去除停用词
words = []
for word in d_words:
    if word not in stop:
        words.append(word)

words=[word.lower() for word in words if word.isalpha()]
#print(words)
#统计词频
freq_ci = []
num,ci = [],[]
freq_word = nltk.FreqDist(words)
#print(freq_word.tabulate(10,cumulative = True))
for key,val in freq_word.items():
    A = (str(key),str(val))
    freq_ci.append(A) 
    ci.append(key)
    num.append(val)
dict_freq_ci = dict(zip(ci,num))

#print(freq_ci)

c = (
    WordCloud()
    .add("", freq_ci, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="Trump"))
    .render("wordcloud_diamond.html")
)


pac_mask = imageio.imread(r'K:\Trump.jpg')
wc = wordcloud.WordCloud(background_color='white',max_words=200,mask=pac_mask).fit_words(dict_freq_ci)
wc.to_file('test.png')

plt.imshow(wc)
plt.axis('off')
plt.show()