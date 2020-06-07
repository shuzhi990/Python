#可视化每个时间段评论数
import re 
import datetime
from collections import Counter
from pyecharts.charts import Line,Bar
from pandas import Series
import pandas as pd
from pyecharts import options as opts
from pyecharts.globals import ThemeType

Time_changed,Hour,Time_Count,Time_Name = [],[],[],[]
f = open('K:\爬虫实例\爬取qq音乐评价\qq_Music_Time.txt',encoding='UTF-8')
for mes in f:
    mes = int(mes)
    mes = datetime.datetime.utcfromtimestamp(mes)
    Time_changed.append(str(mes))

for mes in Time_changed:
    string = list(mes)
    string2 = string[11:13]
    string2 = ''.join(string2)
    Hour.append(string2)

Count = Counter(Hour)
Time_Name = list(Count)
for i in Time_Name:
    Time_Count.append(Count[i])
print(Time_Count)

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
#添加x值，x是一个列表
bar.add_xaxis(Time_Name)
#添加y值，y是一个列表
bar.add_yaxis('出现次数',Time_Count)
#设置主标题、副标题「汉字一文字的外框」
bar.set_global_opts(title_opts=opts.TitleOpts(title="评论时间分布", subtitle="数据来源：qq音乐"),legend_opts=opts.LegendOpts(is_show=False))
#设置生成html文件
bar.render('K:\爬虫实例\爬取qq音乐评价\Time_Bar_Visualization.html')

c = (
    Line()
    .add_xaxis(Time_Name)
    .add_yaxis("商家A",Time_Count, is_smooth=True)
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.25),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="「入海」评论时间分布"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .render("K:\爬虫实例\爬取qq音乐评价\Time_Line_Visualization.html")
)

c = (
    Line()
    .add_xaxis(Time_Name)
    .add_yaxis("商家A", Time_Count, is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="「入海」评论时间分布"),legend_opts=opts.LegendOpts(is_show=False))
    .render("K:\爬虫实例\爬取qq音乐评价\Time_Line_smooth_Visualization.html")
)