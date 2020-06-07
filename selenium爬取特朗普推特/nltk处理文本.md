# 安装nltk

首先安装nltk库

>  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple nltk
>

然后进入python shell执行

> nltk.download()

这步经常会出错，建议不要这么下载，最好下载好nltk_data的包，然后放到C盘根目录下。

最好验证包是否成功安装。

> from nltk.book import *

安装成功的界面如下

![image-20200505145123327](C:\Users\树枝990\AppData\Roaming\Typora\typora-user-images\image-20200505145123327.png)

# 简单文本分析

### 将文本分句`sent_tokenize()`

我使用的文本是前几天爬取的特朗普的推特内容，大概有五百条推特。使用如下代码将文本分句。

```
sents = nltk.sent_tokenize(text)
for sent in sents:
    print(sent)
```

效果如下，我觉得还可以。

![image-20200505145604855](C:\Users\树枝990\AppData\Roaming\Typora\typora-user-images\image-20200505145604855.png)

### 将文本分词`word_tokenize()`

```
words = nltk.word_tokenize(text)
for word in words:
    print(word)
```

效果如下

![image-20200505151830203](C:\Users\树枝990\AppData\Roaming\Typora\typora-user-images\image-20200505151830203.png)

### 统计词数据`FreqDist()`

统计单词数量。

```python
words = nltk.word_tokenize(text)
freq_word = nltk.FreqDist(words)  
#词数量
print(freq_word.N())  
#不重复词数量
print(freq_word.B())
#出现最多的词
print(freq_word.max())
#获得某词的频数
print(freq_word['news'])
#出现次数前n的词,cumulative为True，查看出现次数。
print(freq_word.tabulate(10,cumulative = True))
```

结果如下

```
11425
1965
,
25
   ,  the    !    .   to    a   of    '  and   is
 612  988 1296 1588 1815 2021 2219 2414 2604 2723
```

### 去除停用词

在上面的统计词频中，出现次数前十的词几乎都没有什么价值，所以需要设置一些停用词。NLTK自带了多种语言的停用词列表。

```python
from nltk.corpus import stopwords
stop = stopwords.words('english')
#去除停用词
words = []
for word in d_words:
    if word not in stop:
        words.append(word)
```

但只去除停用词还不够，因为无法去除其中的标点符号。通过下面的代码去除标点符号。

```python
words=[word.lower() for word in words if word.isalpha()]
```

最终得到的出现次数前十的词语为

```
        i      news       the     great president     house     media     white      fake     thank 
       90       170       236       296       356       415       472       522       571       616
```

