#可视化前十的词为漏斗图
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Funnel
from pyecharts.globals import ThemeType

Word = [('毕业', 4465), ('我们', 4087), ('回答', 3985), ('浪花', 1998), ('跃入', 1907), ('自己', 1473), ('一起', 1459), ('成长', 1414), ('未来', 1356), ('生活', 1349), ('江湖', 1301), ('梦想', 1277), ('人海', 1207),('河流', 1114), ('灿烂', 1104)]
Word_Name,Word_Count = [],[]

for i in range(len(Word)):
    Word_Name.append(Word[i][0])
    Word_Count.append(Word[i][1])
print(Word_Name)
print(Word_Count)    
#创建图表并设置主题
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
#添加x值，x是一个列表
bar.add_xaxis(Word_Name)
#添加y值，y是一个列表
bar.add_yaxis('出现次数',Word_Count)
#设置主标题、副标题「汉字一文字的外框」
bar.set_global_opts(title_opts=opts.TitleOpts(title="「入海」评论区出现次数前十五的词", subtitle="数据来源：qq音乐"),legend_opts=opts.LegendOpts(is_show=False))
#设置生成html文件
bar.render('K:\爬虫实例\爬取qq音乐评价\Bar_Visualization.html')

c = (
    Funnel()
    .add(
        "词",
        [list(z) for z in zip(Word_Name[0:9], Word_Count[0:9])],
        label_opts=opts.LabelOpts(position="inside"),  
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="「入海」评论区出现次数前十的词"),legend_opts=opts.LegendOpts(is_show=False))
    .render("K:\爬虫实例\爬取qq音乐评价\Word_funnel.html")
)
